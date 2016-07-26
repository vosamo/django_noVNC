## 在Django中集成noVNC

noVNC是一个用HTML5实现的VNC客户端，通过websockify实现websocket和tcp socket之间的转换。

**注意：**模板文件的修改，主要是静态文件路径的修改；wsgi.py中代理进程的启动。

具体可参考我写的[noVNC的使用之一](http://vosamo.github.io/2016/07/noVNC%E7%9A%84%E4%BD%BF%E7%94%A8%E4%B9%8B%E4%B8%80/)和[noVNC的使用之二(在Django中集成noVNC)](http://vosamo.github.io/2016/07/noVNC%E7%9A%84%E4%BD%BF%E7%94%A8%E4%B9%8B%E4%B8%80/)
