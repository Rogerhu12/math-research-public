# root 全文采纳：direct CSC 字节测试和完整新入口的静态范围

日期：2026-11-10 UTC。会话：Astra-visible-flex-db6f0b0e。
**接受完整静态源码范围；尚未实际运行任何新Python、factory、矩阵、安装、纯准备或solver。**
本文不是新launch，也没有预造任何通过报告。
当前原LU02任务的最终退出仍未知。

## 1. 本次确实全文读过的内容

root完整读取：
- 小字节测试26045B、方法7772B、未执行计划5375B及出版清单；
- 新metadata gate20547B、selector14009B、runner24690B、preparer13103B、auditor31225B；
- 完整方法16153B、变换账本的全部22/12/9项before/after；
- 字节测试完整独审十节、完整入口独审十四节。

每一作者文件都从自身固定commit回读，全文UTF-8字节、Git blob、SHA256与出版清单核同。
不是只读摘要、挑选函数或以审者结论代替阅读。

基础foundation-v2及其纯源码/整数checker的此前root全文采纳仍是
notes/2026-11-09-db6f-root-direct-csc-static-adoption.md，
commit35ee1c233d5e36fa800787869293521fbafbcaa8。
本次没有重新运行或重称这些旧证据。

完整小测试出版清单：
commit de107df51fad5fd41598428f7f04f67863f647a7，
SHA256 89b843c32dd7cb9184aac616aaeca49949c9526a46c5e43be34cb0f36868d019。
完整新入口七件清单：
commit 10b4787a990d03a9e5e5176a9b86e0ba4cff366c，
SHA256 cf131f1574d92b1e315ab13074bf9fd59be3d236b0387e7cf7e114e810ce6b04。

## 2. 未参与者全文独审

字节测试审稿：
notes/2026-11-09-db6f-tail-review-direct-csc-byte-test.md，
commit e4a15f7f830690c13d947ae764c648d445327ec8，
blob c87ee21bac08955228218e3c46db54778ecfff23，14870B，
SHA256 f8c0f68ad9d5a0fc64a7b9962bad754dc8f5dfa315af81bd00bb6350d216cce4。

完整入口审稿：
notes/2026-11-10-db6f-tail-review-direct-csc-full-entry.md，
commit 626b6123f05b37793b85aae640d2bb25810318f2，
blob 2fc8bf80f491350e77b8afd2c48207d3670b5959，20503B，
SHA256 5d305c7fbeb1a4bde4103511d8729dc82816aed10944b9810db68bc52a460f1c。

tail未参与具体实现，全文核对全部新源、旧入口和检查器schema。
其真实V8文本重放为00:22:56的三份完整22/12/9变换，
及00:23:17重新正确抽取后的12函数比较。
审稿透明披露首个辅助抽取器类型错误；错误计数不作为证据。
0Python/AST/factory/矩阵/安装/负门/纯准备/BVP/DN实际执行。

## 3. root复核的核心合同

小测试确实使用固定官方原construct和原indices作为参照，
新版不参与expected的生成。每个Seed复制完整根缓冲后按同一视图布局重建，
所以原/新两个调用彼此独立，内部的部分/完全/负步长/Fortran别名关系保持。
完整CSC三数组的字节、dtype、结构零、符号零及全部调用者副作用都检查；
15例只能支付这组实际实现/环境，不外推任意NumPy子类或所有异常时序。

新入口必须读取两个实际检查报告及root各自实际tool自然退出观察；
source/type/schema、实际解释器、全部六份SciPy源和准确command均重核。
写着PASS的计划、程序请求码或静态审稿不支付这四份实际证据。

selector只改backend.prepare_sys，新闭包捕获新constructor；
原exported construct/indices/solve_bvp保持，Newton由已审release-LU另行负责。
新函数/闭包/helper/CSC类方法与实际测试factory完整对应，
每次BVP核前后身份，finally恢复原prepare。
恢复失败使整个记录失败，不能沿用先前数学success。

M14/N512/W14、原物理g、尾深度12、P8×S32、floor.05、8outer、
原tol2e-9/bc1e-8/physical_bc_tol选项2e-11/max6500均未改变。
首DN、最后自有Jac/audit/seam、真正多项式端高和实际tool退出分开记账；
最终finite coupled PASS仍不是连续整图metric/reach或G5。

## 4. root真实文本执行回执

实际functions.exec于2026-11-10 00:46:47 UTC正常完成，
身份root-direct-csc-full-entry-text-adoption-01。
从固定旧全文按全部替换逐步核出现次数，再核完整新字节：

- runner：22项，24690B，全文相同，SHA256 b6fd772b5f44819186fc7e31af370ffa199bfa5c9b14a2722b36345bcf26cd24。
- preparer：12项，13103B，全文相同，SHA256 2e843363c57aee7d96b3359fc0735604f9c0fdbafce8ad4adb2feb421d4f3116。
- auditor：9项，31225B，全文相同，SHA256 b6222f3394c53eebd8409c922ed2e009de85b4bcdbfa5a6e8c8d57b2294967e0。

12个指定完整函数也各要求唯一非空抽取后逐字相同。
root抽取以trimEnd移除尾随空行；独审对应末三函数保留末换行。
后续V8已逐一确认给root文本增加一个末换行即得到独审所列三个SHA，
因此这是序列化边界差别，不是函数正文差异。

本次没有Python AST、模块导入、函数factory、数组运算、选择/恢复或数值运行。
V8全文检查只证明文本来源和变换，不证明Python动态执行成功。

## 5. 实际环境恢复后的继续顺序

先核旧LU02进程、输出、guard completion与真实退出，不从失联推断OOM或完成。
恢复本地未确认发布的对象，合并远端新证明与H/open后普通终端git推送，
不以旧本地状态覆盖当前记录。

若需要新CSC主任务，先在真实环境实际完成冻结纯checker与15例字节测试，
由root记录真实解释器、准确command、tool receipt、自然退出和完整闭文件身份。
然后实际验证新来源/选择恢复/准备合同；以新stem生成真实launch，
将本采纳和完整独审、实际来源及当时资源条件纳入运行审查。
这些步骤已经属于用户持续研究授权，无须再停下请求常规确认。

不得手造未来positive fixture、借旧入口名称安装新源、
继承另一次试验的成功包，或用静态数组计数保证峰值。
真实G5、成功新候选、整图连续证书、新网格和未参与者原种子完整重跑仍开。
