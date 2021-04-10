# Reseed for NHD
快捷方便的辅种工具

https://github.com/dougefla/Reseed_NHD

## 目前支持站点

- NexusHD

## 更新说明

- beta v3.0
  - 实现网页版的查询界面（http://draw.douge.net.cn）
  - 实现数据库每小时自动更新
  - 支持按文件结构匹配（目前版本未启用）
  - 支持跨平台使用
  - 压缩本地索引软件的大小
  - 修正查询算法中的Bug

- beta v2.0
  - 修改了匹配算法，大大提升速度。
  - 修正了一些匹配逻辑。

![image.png](https://i.loli.net/2021/04/10/8XpcFMO9mWldq5R.png)

## 为什么写这个工具？
手握多个PT站点的玩家而言，辅种是让手上资源发挥最大价值的重要方法。辅种的意思就是，本地硬盘上面已经有某PT站的资源，通过下载这个PT站的相应种子文件进行文件校验后直接做种，不需要重新下载一遍实际的资源文件了。没有自动化工具的时候，跨站辅种意味着需要把硬盘中的资源和PT站点中的资源进行一一手动比较。当手上的资源很多时，这样的操作费时费力。于是就出现了辅种脚本。目前比较成熟的自动化软件是北洋园的Reseed，同时具有前后端，且支持国内一众站点。但是由于众所周知的原因，浙江大学的NexusHD却并未被任何辅种工具所收录。本项目服务N站用户，提供本地资源检索-数据匹配-批量返回种子url的功能。

## 这个工具能做什么？
扫描本地路径，与NHD中存在的资源做比较。若相符，则返回相应的种子文件url。

## 怎么使用？
### 第零步：运行环境
- 一个有效的NexusHD账号
- 一台有待辅种资源的Windows/Linux/Mac电脑
- 互联网连接

### 第一步：本地资源索引
1. 下载[EXE版本](https://github.com/dougefla/Reseed_NHD/blob/main/reseed_beta_v3.0/reseed_beta_v3.0.exe)或[Python版本](https://github.com/dougefla/Reseed_NHD/blob/main/reseed_beta_v3.0/user.py)到任意目录，运行软件。

![image.png](https://i.loli.net/2021/04/10/YO4ADhbpwuonBTj.png)

2. 提示输入【Directory】，请输入您想要检索的根目录。例如想要下面的目录结构，就输入 D:\电影。注意，本程序仅将最外层目录（除了输入的根目录）视为资源名，所有子文件夹下的文件均仅视为资源内容。

```
D:\电影
├──Captain.Marvel.2019.2160p.BluRay.REMUX.HEVC.DTS-HD.MA.TrueHD.7.1.Atmos-FGT
├──Carnage.2011.1080p.BluRay.x264.DTS-WiKi
├──Casa.de.Lava.1994.BluRay.1080p.DTS-HD.MA.1.0.x264-CHD
├──Charade.1963.720p.Blu-ray.AAC.x264-CtrlHD
```
3. 提示输入【Your passkey】。注意不是你的登录密码。可在NHD网站的【控制面板】-【设定首页】-【密钥】中找到。为一由小写字母和数字构成的字符串。
![image.png](https://i.loli.net/2021/04/10/nmu5zrt24EjRd1C.png)


4. 回车确认输入。程序会自动开始索引当前目录。在【程序的同级目录】下生成scan_result.json，即本地索引结果


### 第二步：网页端查询
1. 查询页面为：http://draw.douge.net.cn
2. 点击【选择文件】，选择上一步生成的scan_result.json，然后点击【Upload】。
3. 等待数秒后，在下面的文字框中会显示所有匹配到的种子的下载链接。点击【复制】。

### 第三步：下载.torrent文件并辅种

1. 对于qb用户：获得种子的下载链接后，点击qb的【文件】-【添加torrent链接】，复制进去即可。对于其他用户，可能需要IDM等其他下载工具批量下载对应的.torrent文件。
2. 在弹出的界面选择相应的下载位置。下载软件会自动开始校验。若校验通过则辅种成功。

## 可能的报错
- ERROR：Overtime
  - 超时。可能是服务器正忙，或者后台程序出现异常。若持续出现此错误，请联系管理员。
- ERROR: Cannot Parse Uploaded File
  - 无法解析上传的文件。可能是上传了错误或损坏的文件
- ERROR: Cannot Open Uploaded File
  - 无法打开上传的文件。可能是服务器正忙。
- 上传后无返回值
  - 可能是上传了非.json文件

## 汇报Bug

如果在使用过程中遇到任何Bug或者有任何建议，欢迎通过私信或回帖告诉我~
- CC98: douge
- NexusHD: Douge
