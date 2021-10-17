{{- define "djangocli.backend.fullname" -}}
{{- printf "%s-%s" (include "common.names.fullname" .) "backend" | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "djangocli.nginx.fullname" -}}
{{- printf "%s-%s" (include "common.names.fullname" .) "nginx" | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "djangocli.celeryworker.fullname" -}}
{{- printf "%s-%s" (include "common.names.fullname" .) "celeryworker" | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "djangocli.secret.mariadb.name" -}}
{{- printf "%s-%s" (include "common.names.fullname" .) "secret-mariadb" -}}
{{- end -}}

{{- define "djangocli.secret.redis.name" -}}
{{- printf "%s-%s" (include "common.names.fullname" .) "secret-redis" -}}
{{- end -}}

{{- define "djangocli.secret.image.name" -}}
{{- printf "%s-%s" (include "common.names.fullname" .) "secret-image" -}}
{{- end -}}

{{- define "djangocli.secret.app.name" -}}
{{- printf "%s-%s" (include "common.names.fullname" .) "secret-app" -}}
{{- end -}}

{{- define "imagePullSecret" }}
{{- with .Values.imageCredentials }}
{{- printf "{\"auths\":{\"%s\":{\"username\":\"%s\",\"password\":\"%s\",\"email\":\"%s\",\"auth\":\"%s\"}}}" .registry .username .password .email (printf "%s:%s" .username .password | b64enc) | b64enc }}
{{- end }}
{{- end }}

{{/*
Create the name of the service account to use
*/}}
{{- define "djangocli.serviceAccountName" -}}
{{- if .Values.serviceAccount.create }}
{{- default (include "common.names.fullname" .) .Values.serviceAccount.name }}
{{- else }}
{{- default "default" .Values.serviceAccount.name }}
{{- end }}
{{- end }}


{{/*
Fully qualified app name for MariaDB
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
*/}}
{{- define "djangocli.mariadb.fullname" -}}
{{- printf "%s-%s" .Release.Name "mariadb" | trunc 63 | trimSuffix "-" -}}
{{- end -}}


{{/*
Fully qualified app name for Redis
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
*/}}
{{- define "djangocli.redis.fullname" -}}
{{- printf "%s-%s" .Release.Name "redis" | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Return the Redis host
*/}}
{{- define "djangocli.redis.host" -}}
{{- if .Values.redis.enabled }}
    {{- printf "%s-master" (include "djangocli.redis.fullname" .) -}}
{{- else -}}
    {{- printf "%s" .Values.externalRedis.host -}}
{{- end -}}
{{- end -}}


{{- define "djangocli.commonEnv" -}}
- name: DC_ENV
  value: prod
- name: IS_INJECT_ENV
  value: "False"

- name: DC_MYSQL_NAME
  valueFrom:
    secretKeyRef:
      name: {{ include "djangocli.secret.mariadb.name" . }}
      key: database
- name: DC_MYSQL_HOST
  valueFrom:
    secretKeyRef:
      name: {{ include "djangocli.secret.mariadb.name" . }}
      key: host
- name: DC_MYSQL_PORT
  valueFrom:
    secretKeyRef:
      name: {{ include "djangocli.secret.mariadb.name" . }}
      key: port
- name: DC_MYSQL_USER
  valueFrom:
    secretKeyRef:
      name: {{ include "djangocli.secret.mariadb.name" . }}
      key: username
- name: DC_MYSQL_PASSWORD
  valueFrom:
    secretKeyRef:
      name: {{ include "djangocli.secret.mariadb.name" . }}
      key: password

- name: DC_REDIS_HOST
  valueFrom:
    secretKeyRef:
      name: {{ include "djangocli.secret.redis.name" . }}
      key: host
- name: DC_REDIS_PORT
  valueFrom:
    secretKeyRef:
      name: {{ include "djangocli.secret.redis.name" . }}
      key: port
- name: DC_REDIS_PASSWORD
  valueFrom:
    secretKeyRef:
      name: {{ include "djangocli.secret.redis.name" . }}
      key: password

- name: SECRET_KEY
  valueFrom:
    secretKeyRef:
      name: {{ include "djangocli.secret.app.name" . }}
      key: secretKey
- name: APP_NAME
  valueFrom:
    secretKeyRef:
      name: {{ include "djangocli.secret.app.name" . }}
      key: appName
- name: APP_VERSION
  valueFrom:
    secretKeyRef:
      name: {{ include "djangocli.secret.app.name" . }}
      key: appVersion

- name: DJANGO_SUPERUSER_PASSWORD
  valueFrom:
    secretKeyRef:
      name: {{ include "djangocli.secret.app.name" . }}
      key: superUserPassword
- name: DJANGO_SUPERUSER_USERNAME
  valueFrom:
    secretKeyRef:
      name: {{ include "djangocli.secret.app.name" . }}
      key: superUserName
- name: DJANGO_SUPERUSER_EMAIL
  valueFrom:
    secretKeyRef:
      name: {{ include "djangocli.secret.app.name" . }}
      key: superUserEmail
{{- end -}}
