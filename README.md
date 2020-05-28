<h1>一个神秘的项目</h1>
<p>或许有一个神秘的用处</p>

<a href="http://testhttps.0431zy.com/" rel="nofollow">体验demo</a>

<h3>特点</h3>
<ul>
<li>Python语法</li>
<li>使用flask搭建web环境</li>
<li>使用Blueprint进行模块化处理</li>
<li>使用阿里云服务的oss进行静态文件管理</li>
<li>目前项目只有后台接口</li>
</ul>

<h3>工具的选择</h3>
<ul>
<li>代码编写工具我用的PyCharm，有破解，需要可以找我86131711</li>
<li>接口调试工具用的火狐的RESTClient</li>
</ul>

<h3>接口调用步骤</h3>
<ul>
<li>登录接口
<p>必须首先调用获取token，http://127.0.0.1:5000/user/login，</p>
<p>传入base认证，name：Admin，password：12345，</p>
<p>增加HTTP头字段：Content-Type: application/json</p>
<p>请求方式使用：GET</p>
<p>成功返回：{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwdWJsaWNfaWQiOiI1MjUwYjIxYS02ODAzLTQxNmEtOWE5NC1jN2M2ZjQ0NjIzMDciLCJleHAiOjE1OTA2NTEyMjR9.mD-JL95G1ABTsokfRg29RZTAgzlA0B7JUnZNAIbAJTc"
}
</p>
</li>
<li>获取所有用户
<p>http://127.0.0.1:5000/user</p>
<p>增加HTTP头字段：x-access-token，值是之前获取的token</p>
<p>成功返回：
{
  "message": [{
    "admin": true,
    "name": "Admin",
    "password": "sha256$4sD62F1w$cc35ed0dbb0470db2889e74a50987bcc79b711258f5e2514d36af4fe544c0bb2",
    "public_id": "5250b21a-6803-416a-9a94-c7c6f4462307"
}
</p>
</li>
</ul>

<h3>图片上传</h3>
<ul>
<li>通过Ali提供的接口上传静态文件并获得访问地址
<p>http://127.0.0.1:5000/user/change_avatar/public_id</p>
<p>public_id：使用获取所有用户接口获得</p>
<p>增加HTTP头字段：Content-Type: application/json</p>
<p>增加HTTP头字段：x-access-token，值是之前获取的token</p>
<p>增加正文内容：{"avatar_base_64_str" : "base64的串"}</p>

<p>可以使用 http://tool.chinaz.com/tools/imgtobase/ 获取图片base64的串，要去掉文件头 ”data:image/png;base64,“</p>
</li>
</ul>

<h3>图片上传的活动图</h3>
<img src="http://sunlingfeng.0431zy.com/hdtyd.jpg" width="100%"/>
