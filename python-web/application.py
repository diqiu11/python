#!/usr/bin/env python
# coding=utf-8
#wsgi接口模拟HTTP

def application(environ, start_response):
    start_response('200 OK', [('Content-Type',' text/html')])
    body = '<h1>Hei, %s</h1>' % (environ['PATH_INFO'] or 'web')

    return [body.encode('utf_8')]
