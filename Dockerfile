FROM fedora
MAINTAINER Christian Heimes
RUN dnf -y update && dnf clean all
EXPOSE 8080
ADD debugsrv.py /debugsrv.py
CMD ["/debugsrv.py"]

