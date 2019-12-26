testdata="""<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <title>测试页面</title>



 

</head>

 

<body>

Hello<br>
<button onclick='dosubmitdelete()'>点此删除</button>
<br>
杂乱无章

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
        
        
function urlpage(){
        index=((window.location.protocol)+'//'+location.hostname+('/folder'));
        if ((location.href)==(index)){
            alert ('当前已经在首页了，无法回退');
            }else{
                history.back(-1);
			}
        }
function dosubmitdelete(){
        document.getElementById('submit.delete').style.display='block';
        document.getElementById('submit.delete').click();
        
        
        }
        
        
    </script>


<form name='firstform'action="/test" method="POST">
        <div class="mybox">
            <p>1、请选择你喜欢吃的甜品：</p>
            <input type="hidden" style="visibility: hidden;" name="formname" value="firstform" />
            <input type="checkbox" class="mycheckbox" name='mycheck' value="雪糕"/>雪糕            
            <input type="checkbox" class="mycheckbox" name='mycheck' value="蛋糕"/>蛋糕            
            <input type="checkbox" class="mycheckbox" name='mycheck' value="无"/>无            
        </div>
        <div class="mybox">
            <p>1、请选择你喜欢的运动：</p>
            <input type="checkbox" class="mycheckbox" name='mycheck' value="滑雪"/>滑雪            
            <input type="checkbox" class="mycheckbox" name='mycheck' value="爬山"/>爬山            
            <input type="checkbox" class="mycheckbox" name='mycheck' value="无"/>无            
        </div>
        <div class="mybox">
            <p>1、请选择你喜欢吃的美食：</p>
            <input type="checkbox" class="mycheckbox" name='mycheck' value="烧烤"/>烧烤            
            <input type="checkbox" class="mycheckbox" name='mycheck' value="海鲜"/>海鲜        
            <input type="checkbox" class="mycheckbox" name='mycheck' value="无"/>无            
        </div>
        
        
 
        
        <!--<div><button id="save">提交</button></div>-->
        <input style="visibility: hidden;"id='submit.download'type='submit' name='submit'value='下载'>
        <input style="visibility: hidden;"id='submit.delete'type='submit' name='submit'value='删除'>
        </form>
        
        
        <button onclick='dosubmitdelete()'>点此删除</button>
    </body>

</body>

</html>"""