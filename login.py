#!/usr/bin/python

# coding:utf-8


loginhtm="""<!DOCTYPE html>
<html lang="cn">
<head>
    <meta charset=utf-8"utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="SimpleDrive">
    <meta name="keyword" content="SimpleDrive">
    <link rel="shortcut icon" href="/favicon">

    <title>Simple Drive</title>

    <!-- Bootstrap core CSS -->
    <link href="lib/view/css/bootstrap.min.css"  rel="stylesheet">
    <link href="lib/view/css/bootstrap-reset.css"  rel="stylesheet">
    <!--external css-->
    <link href="lib/view/assets/font-awesome/css/font-awesome.css"  rel="stylesheet" />
    <link href="lib/view/assets/jquery-easy-pie-chart/jquery.easy-pie-chart.css" tppabs="http://www.njwez.com/lib/view/assets/jquery-easy-pie-chart/jquery.easy-pie-chart.css" rel="stylesheet" type="text/css" media="screen"/>
    <link rel="stylesheet" href="lib/view/css/owl.carousel.css"  type="text/css">
    <!-- Custom styles for this template -->
    <link href="lib/view/css/style.css"  rel="stylesheet">
    <link href="lib/view/css/style-responsive.css"  rel="stylesheet" />
    <link href="lib/view/css/index.css"  rel="stylesheet" />
    <link rel="stylesheet" type="text/css" href="lib/view/assets/jquery-multi-select/css/multi-select.css"  />

</head>
<body class="loginBg">
<section id="container">
        <div class="loginLogo"></div>
        <!--sidebar start-->
        <!--sidebar end--><link href="lib/view/css/login.css"  rel="stylesheet" />
    <div class="login">
        <div class="col-lg-10">
		<form action="/login" method="post">
            <div class="input-group m-top20">
                <span class="input-group-addon"><i class="icon-user"></i></span>
                <input type="text" name="username" id="userName" placeholder="请输入用户名" class="logininput form-control input-lg">
            </div>
            <div class="input-group m-top20">
                <span class="input-group-addon"><i class="icon-unlock-alt"></i></span>
                <input type="password" name="password" id="passWord" placeholder="请输入密码" class="logininput form-control input-lg">
            </div>
        </div>
        <div class="col-lg-10">
            <button style="float: left;" class="btn btn-info" type="submit" id="loginbtn">登录</button>
            <div style="float: left;margin-left: 20px;margin-top: 23px;" id="aregist">
                <label>
                    <a href='/signup'target='_blank'>还没有账号？点此注册</a>
                </label>
            </div>

    </div>
</section>


</body>
</html>"""