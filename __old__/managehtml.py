#!/usr/bin/python

# coding:utf-8

cloudhead_manage = """

<!DOCTYPE html>
<html lang="cn">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Simple Drive">
    <meta name="keyword" content="Simple Drive">
    <title>Simple Cloud</title>
    <!-- Bootstrap core CSS -->
    <link href="/pan/css/bootstrap.min.css" rel="stylesheet">
    <link href="/pan/css/bootstrap-reset.css" rel="stylesheet">
    <!--external css-->
    <link href="/pan/css/font-awesome.css" rel="stylesheet" />
    <link href="/pan/css/jquery.easy-pie-chart.css" rel="stylesheet" type="text/css" media="screen"/>
    <!-- Custom styles for this template -->
    <link href="/pan/css/style.css" rel="stylesheet">
    <link href="/pan/css/style-responsive.css" rel="stylesheet" />
    <link href="/pan/css/index.css" rel="stylesheet" />
    <link rel="stylesheet" type="text/css" href="/pan/css/multi-select.css" />
<body >

<script type="text/javascript">
	function folderoff(){
		document.getElementById('folder').style.display='block';
		}
	function fileoff(){
		document.getElementById('file').style.display='block';
		}
	function folderon(){
		document.getElementById('folder').style.display='none';

		}	
	function fileon(){
		document.getElementById('file').style.display='none';

		}

	function showinvitecode(){
		document.getElementById('invitecodeonoff').style.display='block';
		}
	function disshowinvitecode(){
		document.getElementById('invitecodeonoff').style.display='none';

		}
		
	function showregister(){
		document.getElementById('registeronoff').style.display='block';
		}
	function disshowregister(){
		document.getElementById('registeronoff').style.display='none';

		}



function dosubmitdownload(){
        document.getElementById('submit.download').click();}


function dosubmitdelete(){
        document.getElementById('submit.delete').click();
        }
function dosubmitshare(){
        document.getElementById('submit.share').click();

        }


function urlpage(){
        index=((window.location.protocol)+'//'+location.hostname+('/folder'));
        if ((location.href)==(index)){
            alert ('当前已经在首页了，无法回退');
            }else{
                history.back(-1);
			}
        }
    </script>


<section id="container">
    <!--header start-->
    <header class="header white-bg">
                
                <div class="top-nav">
            <ul class="nav pull-right top-menu">
                <li class="dropdown">
                    <a data-toggle="dropdown" class="dropdown-toggle" href="#">

                        <span class="username">用户名："""
afterusername_manage="""                        </span>                        
                    </a>
                </li>
                <li class="dropdown">
                <a  class="dropdown-toggle" href="/logout">
            <span class="username">注销</span>   </a>
            </li> 
            </ul>
        </div>
            </header>
    <!--header end-->
    <!--sidebar start-->
        <aside>
        <div id="sidebar"  class="nav-collapse">
            <!-- sidebar menu start-->
            <ul class="sidebar-menu" id="nav-accordion">
                                <li >
                    <a href="/cloud">
                        <i class="icon-home"></i>&nbsp;
                        <span>资料</span>
                    </a>
                </li>
				<li class="on">
                    <a href="/manage" target='_blank'>
                        <i class="icon-user"></i>&nbsp;
                        <span>管理</span>
                    </a>
                </li>
                <li >
                    <a href="/shared">
                        <i class="icon-user"></i>&nbsp;
                        <span>已分享</span>
                    </a>
                </li>

                            </ul>
            <!-- sidebar menu end-->
        </div>
    </aside>
        <!--sidebar end-->      <!--main content start-->
      <section id="main-content">
          <section class="wrapper">
              <!--state overview start-->
              <div class="row state-overview">
              		<ul class="buttons pull-left">

                    <li>
                            <div id="ucontainer" style="position: relative;">
                                <button class="btn btn-danger"   style="position: relative; z-index: 1;" onClick="#">

                                    待定功能                                </button>
                            <div id="html5_1ds8v1q8j1k2510p7uud11kl15v73_container" class="moxie-shim moxie-shim-html5" style="position: absolute; top: 0px; left: 0px; width: 101px; height: 34px; overflow: hidden; z-index: 0;"><input id="html5_1ds8v1q8j1k2510p7uud11kl15v73" type="file" style="font-size: 999px; opacity: 0; position: absolute; top: 0px; left: 0px; width: 100%; height: 100%;" multiple="" accept=""></div></div>
                        </li>
                  		<li>
                            <div id="ucontainer" style="position: relative;">
                                <button class="btn btn-info"   style="position: relative; z-index: 1;" onclick="fileoff()">

                                    添加用户                                </button>
                            <div id="html5_1ds8v1q8j1k2510p7uud11kl15v73_container" class="moxie-shim moxie-shim-html5" style="position: absolute; top: 0px; left: 0px; width: 101px; height: 34px; overflow: hidden; z-index: 0;"><input id="html5_1ds8v1q8j1k2510p7uud11kl15v73" type="file" style="font-size: 999px; opacity: 0; position: absolute; top: 0px; left: 0px; width: 100%; height: 100%;" multiple="" accept=""></div></div>
                        </li>

						<li>
                            <div id="ucontainer" style="position: relative;">
                                <button class="btn btn-info"   style="position: relative; z-index: 1;" onclick="fileon()">

                                    <<隐藏                                </button>
                            <div id="html5_1ds8v1q8j1k2510p7uud11kl15v73_container" class="moxie-shim moxie-shim-html5" style="position: absolute; top: 0px; left: 0px; width: 101px; height: 34px; overflow: hidden; z-index: 0;"><input id="html5_1ds8v1q8j1k2510p7uud11kl15v73" type="file" style="font-size: 999px; opacity: 0; position: absolute; top: 0px; left: 0px; width: 100%; height: 100%;" multiple="" accept=""></div></div>
                        </li>


                        <li>
                            <button class="btn btn-success" type="button" onclick="dosubmitdelete()" >

                                删除用户                            </button>
                        </li>


                        <li>
                            <button class="btn btn-danger" type="button" onclick='#' >

                                更新用户密码(待开发)                            </button>
                        </li>


                        <li id="share">
                            <a href='/serverstatus' target='_blank'><button class="btn btn-info" type="button"  >

                                服务器状态查询        </button></a>
                        </li>
                        <li id="share">
                            <button class="btn btn-info" type="button" onclick="#" >

                                待定功能                            </button>
                        </li>
                        
                        <li id="share">
                            <button class="btn btn-info" type="button" onclick="showregister()" >

                                开/关注册                            </button>
                        </li>
                        
                        <li>
                            <div id="ucontainer" style="position: relative;">
                                <button class="btn btn-info"   style="position: relative; z-index: 1;" onclick="disshowregister()">

                                    <<隐藏                                </button>
                            <div id="html5_1ds8v1q8j1k2510p7uud11kl15v73_container" class="moxie-shim moxie-shim-html5" style="position: absolute; top: 0px; left: 0px; width: 101px; height: 34px; overflow: hidden; z-index: 0;"><input id="html5_1ds8v1q8j1k2510p7uud11kl15v73" type="file" style="font-size: 999px; opacity: 0; position: absolute; top: 0px; left: 0px; width: 100%; height: 100%;" multiple="" accept=""></div></div>
                        </li>
                        
                        <li id="share">
                            <button class="btn btn-info" type="button" onclick="showinvitecode()" >

                                开关邀请码注册                            </button>
                        </li>
                        <li>
                            <div id="ucontainer" style="position: relative;">
                                <button class="btn btn-info"   style="position: relative; z-index: 1;" onclick="disshowinvitecode()">

                                    <<隐藏                                </button>
                            <div id="html5_1ds8v1q8j1k2510p7uud11kl15v73_container" class="moxie-shim moxie-shim-html5" style="position: absolute; top: 0px; left: 0px; width: 101px; height: 34px; overflow: hidden; z-index: 0;"><input id="html5_1ds8v1q8j1k2510p7uud11kl15v73" type="file" style="font-size: 999px; opacity: 0; position: absolute; top: 0px; left: 0px; width: 100%; height: 100%;" multiple="" accept=""></div></div>
                        </li>
                  </ul>
                  




              </div>
              </div>
              </div>
              <div class="row">
                  <div class="col-lg-12">
                  		<ul class="listTable pull-left">
                            <li id="fileList">
                                <div class="listTableTop pull-left">
                                    <div class="listTableTopL pull-left">

                                        <div id="name" class="name">用户列表<div class="seq"></div></div>
                                    </div>
                                    <div class="listTableTopR5 pull-right hidden-xs">
                                        <div class="size">待定接口1</div>
                                        <div id="status" class="size">待定接口2<div class="seq"></div></div>
                                        <div id="size" class="size">大小<div class="seq"></div></div>
                                        <div id="utime" class="updateTime">是否是管理员<div class="seq"></div></div>
                                    </div>
                                </div>
                            </li>
                            
                            
                            <li  style="display:none" id="invitecodeonoff" onclick="">
							<p>开启或者关闭邀请码注册，此操作优先级低于开/关注册：>>></p>

                                  <form  method="POST" >
                                  <input type="hidden" style="visibility: hidden;" name="formname" value="registerbyinvitecode" />


                           <p>填入数字0代表关闭邀请码注册，填入其他任意值（数字/字母/符号等）代表使用其当作邀请码，邀请码可以用来自动注册，当前值"""
aftercurrentinvitecode="""：</p><input name="invitecode">

                           <input  type=submit value='提交'>
        </form>
                                 </li>
                            
                            
                            
                            <li  style="display:none" id="registeronoff" onclick="">
							<p>开启或者关闭注册新用户，此操作优先于邀请码注册：>>></p>

                                  <form  method="POST" >
                                  <input type="hidden" style="visibility: hidden;" name="formname" value="registerstatus" />


                           <p>此处填入数字1或者0，1代表开启用户注册，0关闭,当前填入数字"""

afteronregister="""：</p><input name="registercode">

                           <input  type=submit value='提交'>
        </form>
                                 </li>
                            
                            
                            
                            
                            <li  style="display:none" id="file" onclick="">
							<p>新建用户>>></p>

                                  <form  method="POST" >
                                  <input type="hidden" style="visibility: hidden;" name="formname" value="newuser" />


                           <p>用户名：</p><input name="username">
                           <p>密码：</p><input name="password" type="password">

                           <input  type=submit value='提交'>
        </form>
                                 </li>



				
                                  <form name='userlit' method="POST">
                                  <input type="hidden" style="visibility: hidden;" name="formname" value="userlist" />

                                  """

filedownloadurla_manage = ("""<li id="li_7544" onclick="">
<div class="listTableIn pull-left" >
                              		<div class="listTableInL pull-left">
                                    <div class="cBox"><input type="checkbox" class="mycheckbox" name='mycheck' value='""")
filedownloadurlb_manage = ("""'/></div>
                                      <div class="name">
                                          <a target="_self"  href=""")
beforefilename_manage = (""" >


                                              
                                              <span class="div_pro">""")
afterfilename_manage = ("""                                                                                           </span>
                                          </a>
                                      </div>
                                  </div>
                                  <div class="listTableInR pull-right hidden-xs">
                                      <div class="size"><a target="_blank" href="#">待定功能</a></div>
                                      <div class="size"><p id="p_7544">待定功能</p></div>
                                      <div class="size">""")
aftersize_manage = ("""</div><div class="updateTime">""")

afterfiletime_manage = ("""</div>
                                      <div style="display:none;position: absolute;margin-left: -60px;" class="float_box" id="box_7544">
                                          <ul class="control">
                                              <li><a title="下载" href="#"><i class="icon-download-alt"></i></a></li>
                                          </ul>
                                      </div>
                                  </div>
                              </div>
                              """)

cloudreset_manage = """
                            <input id='submit.download'style="visibility: hidden;" type='submit' name='submit'value='下载'>
                            <input id='submit.delete'style="visibility: hidden;" type='submit' name='submit'value='删除'>
                            <input id='submit.share'style="visibility: hidden;" type='submit' name='submit'value='分享'>
                           </form>
          </section>
      </section>

      <!--main content end-->
  </section>


</body>
</html>"""
cloudhead_manage = str(cloudhead_manage)
cloudreset_manage = str(cloudreset_manage)
filedownloadurla_manage = str(filedownloadurla_manage)
filedownloadurlb_manage = str(filedownloadurlb_manage)
beforefilename_manage = str(beforefilename_manage)
afterfilename_manage = str(afterfilename_manage)