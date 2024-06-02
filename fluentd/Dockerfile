# fluentd/Dockerfile

FROM fluent/fluentd:v1.16.2-debian-1.1

USER root

RUN ["gem", "install", "fluent-plugin-elasticsearch", "--no-document"]

USER fluent