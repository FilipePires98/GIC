FROM redis:5.0.9-alpine

RUN apk add --quiet --no-cache \
        curl \
        bash

ADD entrypoint.sh /
RUN chmod +x /entrypoint.sh

COPY ./wait-for-it.sh /
RUN chmod +x /wait-for-it.sh

EXPOSE 26379

EXPOSE 9121

ENTRYPOINT ["/entrypoint.sh"]