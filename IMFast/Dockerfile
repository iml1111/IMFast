FROM python:3.11-alpine3.18 as base

COPY ./ /home/IMFast/
WORKDIR /home/IMFast/

RUN apk update && \
	apk add --update --no-cache alpine-sdk gcc libffi-dev && \
	pip install --upgrade pip && \
	pip wheel --wheel-dir=/home/IMFast/wheels -r requirements.txt

FROM python:3.11-alpine3.18

COPY --from=base /home/IMFast/ /home/IMFast/
WORKDIR /home/IMFast/

RUN apk update && \
	apk add --update --no-cache bash curl && \
	mkdir /home/assets && \
	pip install --no-index --find-links=/home/IMFast/wheels -r requirements.txt && \
	rm -rf /home/IMFast/wheels && chmod +x /home/IMFast/imfast.sh

EXPOSE 5000

CMD ["/home/IMFast/imfast.sh", "prod-run"]