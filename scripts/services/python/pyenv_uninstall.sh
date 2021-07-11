BASHRC_PATH="$HOME/.bashrc"
PYENV_ROOT="$HOME/.pyenv/"

echo "task -> uninstall pyenv begin"

rm -rf "$PYENV_ROOT"

echo "removed $PYENV_ROOT"

if [ ! -f "$BASHRC_PATH" ]; then
  echo "Can not find ${BASHRC_PATH}"
  exit 1
fi

sed -i "/^.*pyenv.*/d" "$BASHRC_PATH"
sed -i "/^.*PYENV.*/d" "$BASHRC_PATH"

echo "removed config in $BASHRC_PATH"

echo "task -> uninstall pyenv finished"
