# -*- coding: utf-8 -*-

import os
from pathlib import Path
from typing import Any, Dict

import dotenv

from djangocli.utils.string import str2bool


def get_env(key: str, default: Any = None, _type: type = str, exempt_empty_str: bool = False) -> Any:
    """
    获取环境变量，解决os.getenv(key, default)在变量值为空串时导致default值不生效的问题
    :param key: 变量名
    :param default: 默认值，若获取不到环境变量会默认使用该值
    :param _type: 环境变量需要转换的类型，不会转 default
    :param exempt_empty_str: 是否豁免空串
    :return:
    """
    value = os.getenv(key) or default
    if value == default:
        return value

    if isinstance(value, str) and not value and exempt_empty_str:
        return value

    if _type == bool:
        return str2bool(value)

    try:
        value = _type(value)
    except TypeError:
        raise TypeError(f"can not convert env value to type -> {_type}")

    return value


def get_env_name__value_map(environ_sh_path: str) -> Dict[str, str]:
    """
    获取environ.sh文件中的k-v值
    :param environ_sh_path:
    :return:
    """

    with open(file=environ_sh_path, mode="r", encoding="utf-8") as environ_sh_reader:
        lines = environ_sh_reader.readlines()

    env_name__value_map = {}
    for line in lines:
        if not line.startswith("export "):
            continue
        # remove `export`
        line = line.replace("export ", "")

        # remove "-1"
        if line.endswith("\n"):
            line = line[:-1]

        env_name, value_untreated = line.split("=", 1)

        # remove quote
        if len(value_untreated) >= 2 and value_untreated[0] == value_untreated[-1] == '"':
            value = value_untreated[1:-1]
        else:
            value = value_untreated

        env_name__value_map[env_name] = value
    return env_name__value_map


def generate_envfile(environ_sh_path: str) -> str:
    """
    通过给定的environ.sh文件生成对应的env文件
    :param environ_sh_path:
    :return: .env文件位置
    """
    env_name__value_map = get_env_name__value_map(environ_sh_path)

    envfile_root = Path(environ_sh_path).resolve().parent
    envfile_path = f"{envfile_root}/environ.env"
    with open(envfile_path, "w+", encoding="utf-8") as env_file_writer:
        for env_name, value in env_name__value_map.items():
            env_file_writer.write(f"{env_name}={value}\n")

    return envfile_path


def inject_env(environ_sh_path: str) -> None:
    """
    注入.sh环境变量
    :param environ_sh_path:
    :return:
    """
    env_file_path = generate_envfile(environ_sh_path=environ_sh_path)
    dotenv.load_dotenv(dotenv_path=env_file_path)

    if not get_env("DC_KEEP_ENVFILE", False, _type=bool):
        os.remove(env_file_path)
