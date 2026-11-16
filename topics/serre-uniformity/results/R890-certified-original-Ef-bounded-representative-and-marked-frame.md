# R890：原 E_f 的八步完整有界代表及固定 t 首项的实际认证

日期：2026-11-16。会话：serre-public-astra-20261115。

**状态：本项实际完成。** 八次原除子运算均取得完整418维空间及主函数DAG；末代表 \(D_E\) 有效、次数272、避原 \(P_0\)，并有
\[
\boxed{E_f-1206P_0=(D_E-H)+\operatorname{div}Q_E.}
\tag{890.C.1}
\]
原主函数在固定 \(\rho=z-z_0\) 与 \(t=a^3\) 下的首项均实际计算，原单位没有缩为1。

实际 [run43853462674](https://github.com/Rogerhu12/math-research-public/actions/runs/43853462674)，compute job133251774019，sourceaa00d76e4a0292f780406c5f75090668a9b66523；run receipt于2026-11-16T11:30:10.337643+00:00结束，core用时1874.06585011秒，exit0。56件原输入直接复用，八个完整flip共9228完成数学阶段。结论限于本原 \(E_f\) 的有界RR输入与主函数，不表示原五个Lj或高度已完成。

## 1. 原输入与八步的真实系数

方法为[原八flip与标记帧](../notes/R890-original-eight-flip-Ef-and-marked-frame-method.md)。原 \(D^*,C^*,D_\chi\) 的三个418空间分别来自R880、R887、R872，原Krylov、W、P0正常值、273jets及R883的 \(t/\rho\) 输入均直接消费，未重做。

记
\[
c=C^*-H,\qquad d=D^*-H,\qquad x=D_\chi-H.
\]
节点标签D、Cstar、X分别代表这三个原有效除子，H是原中性代表。表中三元组是相对 \((c,d,x)\) 的**原类系数**，不与名称C混淆。所有模值均在辅助素数1000000753。

|新节点|左右原节点|原类系数|实际使用左锚列数|q(P0)|累计F(P0)|
|---|---|---|---:|---:|---:|
|A|D, D|(0,-2,0)|399|784948304|836333412|
|B|A, H|(0,2,0)|3|669102261|572991073|
|C|B, D|(0,-3,0)|3|125437682|398559495|
|D2|X, X|(0,0,-2)|3|249360437|532155672|
|E|D2, D2|(0,0,4)|3|676749790|821516186|
|F|Cstar, C|(-1,3,0)|399|879986265|687149090|
|G|F, E|(1,-3,-4)|3|889399945|708970107|
|DE|G, H|(-1,3,4)|3|130676821|426403642|

表中锚列数来自各次实际complete-product-image阶段。A和F确实沿冻结的原基顺序走过399列，其余各3列；没有把已做扫描替换为事后更短的挑选。各次产品像均达到真实962维。较大的扫描输出只在一日artifact中，后续可对已完成闭合证书作原bytes保留，不重新做已成产品。

末节点DE的类系数为 \((-1,3,4)\)，与原
\[
E_f-1206P_0=-c+3d+4x+\operatorname{div}\widetilde Q
\tag{890.C.2}
\]
准确一致。

## 2. 每个完整 flip 的数学证书

每步从两个完整 \(W_{D_i}=H^0(3H-D_i)\)、维418的原空间开始。其乘积落在
\[
H^0(6H-D_1-D_2),\qquad \dim=962.
\]
原七个完整纤维的长度1904大于 \(\deg(6H)=1632\)，对整个V6单射，保全部Artin重数。程序按原左锚列依次形成与右418空间的产品，用增量Schur扩张实际选定像及单位逆，真实达到962后才认定乘法像完整。旧span的逆不重新消元，不生成全部418×418对。

随后对原两锚 \(\tau^3,\sigma^3\) 形成完整1884×690约束。两锚无共同零，所以同时属于上述乘法像等价于原V3截面沿 \(D_1+D_2\) 消失。实际秩544，取得完整146维
\[
U=H^0(3H-D_1-D_2).
\]
每一步保存全部1884×146乘回，不以单条候选代替整个核。

从U选原 \(P_0\) 值为单位的未缩放截面u，定义
\[
D_{\rm new}=\operatorname{div}_{3H}(u)-D_1-D_2.
\]
该除子有效、次数272且避P0。第二锚的真实962单位图及全部1904×418关系，再给完整
\[
W_{D_{\rm new}}=H^0(3H-D_{\rm new}),\quad\dim=418.
\]
八个complete-flip证书的实际962/146/418字段、全部1884×146关系及全部1904×418关系均为完成。准确特征零对象由原单位子式表达式定义；模数组不冒称展开的有理或L坐标。

## 3. 主函数方向与全部原单位

每步保
\[
q=u/\tau^3,\qquad
(D_1-H)+(D_2-H)+(D_{\rm new}-H)=\operatorname{div}q.
\tag{890.C.3}
\]
若 \(\kappa_i=(D_i-H)+\operatorname{div}F_i\)，则新类及主函数必须为
\[
\kappa_{\rm new}=-\kappa_1-\kappa_2,\qquad
\boxed{F_{\rm new}=(qF_1F_2)^{-1}.}
\tag{890.C.4}
\]
相同左右父节点出现时，两个因子保留两次；不作集合去重。上表全部q(P0)及累计F(P0)取原未缩放值，每次逆乘积均实际验证。原函数DAG同时记录原u坐标、左右完整空间、父函数及准确除子恒等式。

由(890.C.2)和末类的准确表达式，
\[
\boxed{Q_E=\widetilde Q\,F_{\rm DE}.}
\tag{890.C.5}
\]
这一步取正乘，不能反用 \(F_{\rm DE}\) 或把一个辅助单位忽略。八个F在P0均为原单位，末
\[
F_{\rm DE}(P_0)=426403642.
\]

## 4. 实际固定局部参数首项

原R887 \(\widetilde Q\) 的ρ阶为−1205、首项267133051。原R883给
\[
t=c\rho+O(\rho^2),\qquad c=354813668,\qquad
c^{1205}=201313487.
\]
本次在同一原辅助素点实际形成
\[
\boxed{
Q_E=73437482\,\rho^{-1205}(1+O(\rho))
   =445609902\,t^{-1205}(1+O(t)).
}
\tag{890.C.6}
\]
其准确首项表达式仍为原 \(\widetilde Q\) 首项、原 \(F_{\rm DE}(P_0)\) 及原 \(c^{1205}\) 的正乘DAG；特征零大标量未展开。模值为单位不表示41处单位，原 \(\theta/82\)、P0分支和微分尺度均未再归一化。

标记主函数阶段
R890-original-Ef-bounded-representative-and-marked-principal-QE.json.gz
为5949B / 7f8bfa2c5175ad979430f831ef665e411f3cba1b9cda67dcc5f314282e488a89。
它真实标记actual_original_t_frame_evaluated=true；保原t首项来源136dd22c3aaddb0b650a5513eefd6db70bfee8a088f0f0cd437a5b6927f6094a，不需要新的t jets。

## 5. 完整空间和节点出口

第k节点的完整空间basename为R890-flip-kk-LABEL-complete-normal418-space.json.gz，其中kk与标签按下表顺序为01-A、02-B、03-C、04-D2、05-E、06-F、07-G、08-DE。每件保存690×418正常V3坐标及原unit-solve来源。

|节点|字节|SHA-256|
|---|---:|---|
|A|1165021|e4933d3cab604ea64e791cb230d11222bef5d43df6bf41d7c25b775e3175801f|
|B|1165112|0aace17346d50d9bd384e8a1181962f881d1a37c624765bd6b6b124282385092|
|C|1165201|917373cb973c8717f58eaeecdc0c46caed7103bbdb1e1eab44d82177e008271b|
|D2|1165604|5027d7b098204f09e2c1b87e74823e9cfa5dc22e9324cdc61a003c32bff93559|
|E|1165011|18386d31511233e0c84e2114e3620f71ca15d48a8c916c8953e380fbbf2debe8|
|F|1164761|51f0a9baf86952306c53999910029753b9289e75dab6c36af93b4897d0169b62|
|G|1165462|8a128231f6de9607dcd95cbb79a576ab9ca24dfde72548c0e70cc00919bfd224|
|DE|1165341|859ca655727078d0a5361b9e7879ccb9bda546c7a734c49cd5ec78e1f34905c8|

完整节点出口的相同前缀后接-complete-flip-certificate.json.gz：

|节点|字节|SHA-256|
|---|---:|---|
|A|4892|8fb284d37026245edb1667ff50e2cafb5668e6c0b7069436bf269c157e2d4e9f|
|B|5011|116a109a399c3284be9d2f7dda47fc6359e14d8daec4eee181381e12d4f08c69|
|C|4954|51cc44e5d5919a8699ce08cab7ddf221ab3116e9a0bc2a3062dfeb7d9c842b81|
|D2|4883|c8008a9f419a518e6a1e7b91b89cde0a6f150ff16f373ce061751683b9595d23|
|E|4953|cdce3ef46d9c8c556fdf26a44997f51eb445976a363a4284870f1b9f18798313|
|F|4944|0f8afcdc7164fac996ef51833e31d938dfff3eb231b21a31272310d465e7fc50|
|G|4996|c308cd5cf1aa30393d9caacd451fcb2990f6f85760a1411b4ba5b69e7a12038c|
|DE|5018|9dfc20deaae3eb2f22bc5cf704216faf7c995fd9bce257b9d04e249cac18f1b4|

各出口完整绑定乘法像、会员约束、U146、未缩放u、最终418及principal阶段。下游R894直接复用已成D2/E的原418、原u与累计F；不能只复制其类系数或换新的规范后仍称同一个原节点。

## 6. 实际来源、计算和必要读取

入口为[原核心](../scripts/R890_original_Ef_eight_flip_and_marked_frame.py)与原方法/请求，原run的public-actions-input精确绑定执行文件。核心56130B / da8498fc6ab0f143ba347f4a7dec91c7474bbe2520c349bf33a84bba8e65420f；包装器58151B / 5a5e706d11d3b61a6af7acadd4624f7f1e398afe02e6ee77c339fcf7b01f57f1。数学配置75267c1ba5c7b60c69d22b6a4359a564c7636706b99be9dff781959523155f8e。

|项目|字节|SHA-256|
|---|---:|---|
|最终数学证书|12331|986e2ea9a0015eec7842c8b678610fc143986472a7eb8f77d6708eef52080793|
|来源审计|4520|a9d4e39f3704f9958e4980d40120e646476e1ef0c55658fe7b72986b29fd6030|
|9228阶段manifest|467846|a97a12f436d2df82a3bd9f6c9a15bdd11c556658c7bf20c4bc8830352c8e2feb|
|全输出manifest，9239项|1451468|d51ef99be161206ab53cb00fd1807e200915305f5e06602ab93dd06af8f09a00|
|core receipt|10166|f0f7681b97eb6bedf37a7426572f48b956d4752ae809a54b9289b6df61f79c84|
|run receipt|611|410bc12d19777db98a3de37dd7e93fb6e18466826ed72e1c440e6045c4b4c8aa|
|56件原输入bundle|21816968|16446595a648183151560d6060350c8b692e727fb4a3acbd719e68a87b2562d3|
|原source inventory|26817|f96cf226055895758f48e1d48d8b4a87c1a7bad68951b29d6df7d0ecd41100da|

原一日artifact14222786594，名称serre-global-R890-eight-flip-Ef-43853462674-1，
3818946840B / c5e609ffdbcdaf1247dc33da59a4e74bc4bfabe63e8abfae8002569e0fb6ca41，
到期2026-11-17T11:33:48Z。所有新数学在本公开仓库Actions完成。

根会话必要只读IO [run43860838780](https://github.com/Rogerhu12/math-research-public/actions/runs/43860838780)，job133276973860，sourcefc4fa39cb817c093ef870cb168222670612163fc，共37次Range、33760583B，读取45个所需成员及原全manifest/reference。包括八个小完整出口、八个principal与产品索引、QE、R894所需D2/E原418和u、原七正常V3纤维、中性H与56件旧来源bundle。每个选定成员核原bytes/SHA，没有下载或声称重哈希整个3.8GB archive，也没有重新运行数学。

该45件输入tar为30951546B / 4a307ff22a105f057dfecdfa4cdae82197100b217e877a74beb498b4e2c205ef；
一日artifact14222928598为31320925B / 721e2601fdbcbe3d035a18b69c9c1905731496201cd88cc3352a97a8bf0e2fba，
到期2026-11-17T11:48:03Z。R894和R896各取必要原件复用；raw不进Git、Release或悬空Git对象。

## 7. 已关闭的缺口与仍开放的原任务

原 \(E_f-1206P_0\) 的一个完整有界代表、原主函数及固定t首项现已实际取得。R894所需共同4x节点有真实D2/E来源，可把其18步trace构造减少为16个新节点。R896按实际共同节点复用已成正常V3评价，不重旧评价。

本项未计算另六个Ef的八步有界代表、七项trace最终代表或K下降基、五个真实Lj的128/144空间、原Hecke支持、Poincaré连接、eη/d/N、全nonp项、周期或高度。上述成功不能替代README主目标；Serre一致性继续OPEN。
