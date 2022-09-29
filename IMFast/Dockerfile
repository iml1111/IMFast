FROM python:3.9-alpine as base

COPY ./ /home/IMFast/
WORKDIR /home/IMFast/

RUN apk update && \
	pip install --upgrade pip && \
	pip wheel --wheel-dir=/home/IMFast/wheels -r requirements.txt

FROM python:3.9-alpine

COPY --from=base /home/IMFast/ /home/IMFast/
WORKDIR /home/IMFast/

RUN apk update && \
	apk add --update --no-cache bash curl && \
	mkdir /home/assets && \
	pip install --no-index --find-links=/home/IMFast/wheels -r requirements.txt && \
	rm -rf /home/IMFast/wheels

EXPOSE 5000

CMD ["/home/IMFast/imfast.sh", "prod-run"]