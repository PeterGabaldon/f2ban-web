FROM nginx:latest

COPY dist/ /root/dist/

RUN chown root:www-data -R /usr/share/nginx/html && \
    chmod 755 -R /usr/share/nginx/html && \
    rm -rf /etc/nginx/conf.d/* /usr/share/nginx/html/* && \
    mkdir -p /etc/nginx/conf.d && \
    cp /root/dist/conf/nginx.conf /etc/nginx/ && \
    cp -R /root/dist/conf/ssl /etc/nginx/ && \
    cp /root/dist/conf/f2ban-web.conf /etc/nginx/conf.d/ && \
    rm -rf /root/*

CMD nginx -g 'daemon off;'
