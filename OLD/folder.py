#!/usr/bin/python

# coding:utf-8

cloudhead="""

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
                    <a  class="dropdown-toggle" href="#">
                    
                        <span class="username">用户名："""
preusername="""</span>                      
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
                                <li class="on">
                    <a href="/cloud">
                        <i class="icon-home"></i>&nbsp;
                        <span>资料</span>
                    </a>
                </li>"""
adminpage="""<li >
                    <a href="/manage" target='_blank'>
                        <i class="icon-user"></i>&nbsp;
                        <span>管理</span>
                    </a>
                </li>"""
afteradminpage="""                <li >
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
                                <button class="btn btn-danger"   style="position: relative; z-index: 1;" onClick="urlpage()">
                                    
                                    返回上一页                                </button>
                            <div id="html5_1ds8v1q8j1k2510p7uud11kl15v73_container" class="moxie-shim moxie-shim-html5" style="position: absolute; top: 0px; left: 0px; width: 101px; height: 34px; overflow: hidden; z-index: 0;"><input id="html5_1ds8v1q8j1k2510p7uud11kl15v73" type="file" style="font-size: 999px; opacity: 0; position: absolute; top: 0px; left: 0px; width: 100%; height: 100%;" multiple="" accept=""></div></div>
                        </li>
                  		<li>
                            <div id="ucontainer" style="position: relative;">
                                <button class="btn btn-info"   style="position: relative; z-index: 1;" onclick="fileoff()">
                                    
                                    显示上传文件                                </button>
                            <div id="html5_1ds8v1q8j1k2510p7uud11kl15v73_container" class="moxie-shim moxie-shim-html5" style="position: absolute; top: 0px; left: 0px; width: 101px; height: 34px; overflow: hidden; z-index: 0;"><input id="html5_1ds8v1q8j1k2510p7uud11kl15v73" type="file" style="font-size: 999px; opacity: 0; position: absolute; top: 0px; left: 0px; width: 100%; height: 100%;" multiple="" accept=""></div></div>
                        </li>
						
						<li>
                            <div id="ucontainer" style="position: relative;">
                                <button class="btn btn-info"   style="position: relative; z-index: 1;" onclick="fileon()">
                                    
                                    <<隐藏                                </button>
                            <div id="html5_1ds8v1q8j1k2510p7uud11kl15v73_container" class="moxie-shim moxie-shim-html5" style="position: absolute; top: 0px; left: 0px; width: 101px; height: 34px; overflow: hidden; z-index: 0;"><input id="html5_1ds8v1q8j1k2510p7uud11kl15v73" type="file" style="font-size: 999px; opacity: 0; position: absolute; top: 0px; left: 0px; width: 100%; height: 100%;" multiple="" accept=""></div></div>
                        </li>
						
						
                        <li>
                            <button class="btn btn-success" type="button" onclick="folderoff()" >
                                
                                显示新建文件夹                            </button>
                        </li>
						
						<li>
                            <button class="btn btn-success" type="button" onclick="folderon()" >
                                
                                <<隐藏                            </button>
                        </li>
                        <li>
                            <button class="btn btn-danger" type="button" onclick='dosubmitdelete()' >
                               
                                删除                            </button>
                        </li>
                        
                        
                        <li id="share">
                            <button class="btn btn-info" type="button" onclick="dosubmitdownload()" >
                              
                                下载                            </button>
                        </li>
                        <li id="share">
                            <button class="btn btn-info" type="button" onclick="dosubmitshare()" >
                              
                                分享                            </button>
                        </li>
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
      
                                        <div id="name" class="name">名称<div class="seq"></div></div>
                                    </div>
                                    <div class="listTableTopR5 pull-right hidden-xs">
                                        <div class="size">待定接口1</div>
                                        <div id="status" class="size">待定接口2<div class="seq"></div></div>
                                        <div id="size" class="size">大小<div class="seq"></div></div>
                                        <div id="utime" class="updateTime">上传时间<div class="seq"></div></div>
                                    </div>
                                </div>
                            </li><li  style="display:none" id="file" onclick="">
							<p>在此目录上传新文件>>></p>

                                  <form  method=post enctype=multipart/form-data>
                                  <input type="hidden" style="visibility: hidden;" name="formname" value="newfile" />
	  
          
                           <input  type=file name=file>
  
                           <input  type=submit value='上传'>
        </form>
                                 </li>
							  
							  
							  
							  <li  style="display:none" id="folder" onclick="">

                              		<p>在此目录新建文件夹>>></p>
                                  <form  method="post">
	   
                                <input type="hidden" style="visibility: hidden;" name="formname" value="newfolder" />
                              <p><input  name="newfoldername"></p>
                            <p><button  type="submit">新建</button></p></form>
                                  </li>
                                  <form name='fileorfolderlist' method="POST">
                                  <input type="hidden" style="visibility: hidden;" name="formname" value="fileorfolderlist" />
                                  
                                  """

filedownloadurla=("""<li id="li_7544" onclick="">
<div class="listTableIn pull-left" >
                              		<div class="listTableInL pull-left">
                                    <div class="cBox"><input type="checkbox" class="mycheckbox" name='mycheck' value='""")
filedownloadurlb=("""'/></div>
                                      <div class="name">
                                          <a target="_self"  href=""")
beforefilename= (""" >
                            

                                              
                                              <span class="div_pro">""")
afterfilename= ("""                                                                                           </span>
                                          </a>
                                      </div>
                                  </div>
                                  <div class="listTableInR pull-right hidden-xs">
                                      <div class="size"><a target="_blank" href="#">待定功能</a></div>
                                      <div class="size"><p id="p_7544">待定功能</p></div>
                                      <div class="size">""")
aftersize=("""</div><div class="updateTime">""")



afterfiletime=("""</div>
                                      <div style="display:none;position: absolute;margin-left: -60px;" class="float_box" id="box_7544">
                                          <ul class="control">
                                              <li><a title="下载" href="#"><i class="icon-download-alt"></i></a></li>
                                          </ul>
                                      </div>
                                  </div>
                              </div>
                              """)

cloudreset="""
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
cloudhead=str(cloudhead)
cloudreset=str(cloudreset)
filedownloadurla=str(filedownloadurla)
filedownloadurlb=str(filedownloadurlb)
beforefilename=str(beforefilename)
afterfilename=str(afterfilename)