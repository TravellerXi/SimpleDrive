#!/usr/bin/python

# coding:utf-8

cloudhead_shared = """

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
		




function dosubmitforvershare(){
        document.getElementById('submit.forevershare').click();}


function dosubmitcancelshare(){
        document.getElementById('submit.cancelshare').click();

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
    <script type="text/javascript">
    var returnhostname=document.write(location.hostname);}
    </script>


<section id="container">
    <!--header start-->
    <header class="header white-bg">
               
                <div class="top-nav">
            <ul class="nav pull-right top-menu">
                <li class="dropdown">
                    <a data-toggle="dropdown" class="dropdown-toggle" href="#">

                        <span class="username">用户名： """
preusername_shared="""</span>                        
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
                        <i class="icon-user"></i>&nbsp;
                        <span>资料</span>
                    </a>
                </li>"""
adminpage_shared="""				<li >
                    <a href="/manage" target='_blank'>
                        <i class="icon-user"></i>&nbsp;
                        <span>管理</span>
                    </a>
                </li>"""
afteradminpage_shared="""                <li class="on">
                    <a href="/shared">
                        <i class="icon-home"></i>&nbsp;
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
                                <button class="btn btn-info"   style="position: relative; z-index: 1;" onclick="location.href='/share'">

                                    待定接口                                </button>
                            <div id="html5_1ds8v1q8j1k2510p7uud11kl15v73_container" class="moxie-shim moxie-shim-html5" style="position: absolute; top: 0px; left: 0px; width: 101px; height: 34px; overflow: hidden; z-index: 0;"><input id="html5_1ds8v1q8j1k2510p7uud11kl15v73" type="file" style="font-size: 999px; opacity: 0; position: absolute; top: 0px; left: 0px; width: 100%; height: 100%;" multiple="" accept=""></div></div>
                        </li>
                  		<li>
                            <div id="ucontainer" style="position: relative;">
                                <button class="btn btn-info"   style="position: relative; z-index: 1;" onclick="dosubmitforvershare()">

                                    设为永久分享                                </button>
                            <div id="html5_1ds8v1q8j1k2510p7uud11kl15v73_container" class="moxie-shim moxie-shim-html5" style="position: absolute; top: 0px; left: 0px; width: 101px; height: 34px; overflow: hidden; z-index: 0;"><input id="html5_1ds8v1q8j1k2510p7uud11kl15v73" type="file" style="font-size: 999px; opacity: 0; position: absolute; top: 0px; left: 0px; width: 100%; height: 100%;" multiple="" accept=""></div></div>
                        </li>
                        

						<li>
                            <div id="ucontainer" style="position: relative;">
                                <button class="btn btn-danger"   style="position: relative; z-index: 1;" onclick="dosubmitcancelshare()">
                                    取消共享
                                                                    </button>
                            
                  </ul>
                  <form  method=post>
                      <div class="searchRight pull-right hidden-xs">
                          <div class="input-group m-bot15">
                              <div class="input-group-btn">
                                  
                                      <span id="searchShow" class="btn dropdown-toggle btn-white">名称</span>

                                 
                                 
                              </div>
							  <input type="hidden" style="visibility: hidden;" name="formname" value="search" />
                              <input type="text" class="form-control" id="search" name="search" value="" placeholder="搜文件/文件夹">
                          </div>
                          <button class="btn btn-success searchButton" type="submit">
                              <i class="icon-search"></i>
                              搜索                          </button>
                      </div>
                  </form>




              </div>
              </div>
              </div>
              <div class="row">
                  <div class="col-lg-12">
                  		<ul class="listTable pull-left">
                            <li id="fileList">
                                <div class="listTableTop pull-left">
                                    <div class="listTableTopL pull-left">

                                        <div id="name" class="name">文件(夹)名>>>(右击复制链接即可获得下载地址)<div class="seq"></div></div>
                                    </div>
                                    <div class="listTableTopR5 pull-right hidden-xs">
                                        <div class="size">类型</div>
                                        <div id="status" class="size">实际文件位置<div class="seq"></div></div>
                                        <div id="size" class="size">大小<div class="seq"></div></div>
                                        <div id="utime" class="updateTime">过期时间<div class="seq"></div></div>
                                    </div>
                                </div>
                            </li>



							  
                                  <form name='fileorfolderlist' method="POST">
                                  <input type="hidden" style="visibility: hidden;" name="formname" value="fileorfolderlist" />

                                  """

filedownloadurla_shared = ("""<li id="li_7544" onclick="">
<div class="listTableIn pull-left" >
                              		<div class="listTableInL pull-left">
                                    <div class="cBox"><input type="checkbox" class="mycheckbox" name='mycheck' value='""")
filedownloadurlb_shared = ("""'/></div>
                                      <div class="name">
                                          <a target="_blank"  href=""")
beforefilename_shared = (""" >


                                              
                                              <span class="div_pro">""")
afterfilename_shared = ("""                                                                                           </span>
                                          </a>
                                      </div>
                                  </div>
                                  <div class="listTableInR pull-right hidden-xs">
                                      <div class="size"><a target="_blank" href="#">""")
afterposition_shared=("""</a></div>
                                      <div class="size"><p id="p_7544">""")
position=("""                                     </p></div>
                                      <div class="size">""")
aftersize_shared = ("""</div><div class="updateTime">""")

afterfiletime_shared = ("""</div>
                                      <div style="display:none;position: absolute;margin-left: -60px;" class="float_box" id="box_7544">
                                          <ul class="control">
                                              <li><a title="下载" href="#"><i class="icon-download-alt"></i></a></li>
                                          </ul>
                                      </div>
                                  </div>
                              </div>
                              """)

cloudreset_shared = """
                            <input id='submit.forevershare'style="visibility: hidden;" type='submit' name='submit'value='设为永久分享'>
                            <input id='submit.cancelshare'style="visibility: hidden;" type='submit' name='submit'value='取消分享'>
                           </form>
          </section>
      </section>

      <!--main content end-->
  </section>


</body>
</html>"""
cloudhead_shared = str(cloudhead_shared)
cloudreset_shared = str(cloudreset_shared)
filedownloadurla_shared = str(filedownloadurla_shared)
filedownloadurlb_shared = str(filedownloadurlb_shared)
beforefilename_shared = str(beforefilename_shared)
afterfilename_shared = str(afterfilename_shared)