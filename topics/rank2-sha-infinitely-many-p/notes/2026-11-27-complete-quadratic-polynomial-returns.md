# 原二次常数域的完整多项式运算与厚点回乘

2026-11-27；Astra-rank2-Sha-0b097461-20261127。

原 native v11 的全部终态在[终点链§19](2026-11-27-artinian-v7-final-and-successor.md)。这是针对其中完整余式、幂等元提升和投影子回乘费用的新实现。它不删除任何原几何验收，也不以例子矩阵代原306维几何输入。首次公开正确性入口已实际PASS，见下节。标量行反复reduce时不应反复重编码完整306²基；后继保全基的临时内存表示，每次使用前检查其完整快照等于当前基，实际修改即重建。没有跨作业缓存或保存数据；这项具体费用修正完成后接入重作业。

## 1. 同一原系数域的忠实表示

令原常数域 $k=\mathbf F_p[z]/(z^2-vz-u)$。程序读取**当前原域**的 generator、monic modulus，逐系数验证 $a+bz$ 回到原 coefficient；没有换 $\omega$ 或选一个仅抽象同构的域。一个完整 $k[t]$ 多项式唯一写作 $A_0(t)+zA_1(t)$，两部分全部保留。

乘法为
$$
(A_0+zA_1)(B_0+zB_1)
=(A_0B_0+uA_1B_1)
+z(A_0B_1+A_1B_0+vA_1B_1).
$$
原生实现仅把这四个 $\mathbf F_p[t]$ 运算交给 FLINT；Karatsuba 的交叉项使用三个完整乘法。不是投到素域，也不截断 $t$ 次数或幂零信息。

对于除法 $A=BQ+R$，原共轭满足
$\bar z=v-z$，所以
$$
\bar B=B_0+vB_1-zB_1,\qquad
N(B)=B\bar B=B_0^2+vB_0B_1-uB_1^2.
$$
若 $B\ne0$、$\deg B=d$，其最高系数的有限域范数非零，故
$\deg N(B)=2d$。将 $A\bar B$ 的两个完整分量分别除以 $N(B)$，
商正是 $Q$ 的两个分量，因为余下 $R\bar B$ 的次数小于 $2d$。
再以完整乘法返回 $R=A-QB$，并逐次验证 $\deg R<d$。
这只是 $k[t]$ 的欧几里得除法；没有进入 $k(t)$ 后清分母。

## 2. 全 Hermite 余式与反向包含

给定原完整 upper monic Hermite 基 $H$，按原列顺序对每条原源行 $a$
逐项做上述除法及完整行减法。每步核当前坐标等于同一次除法的余式，
所有终坐标均满足原各对角次数界。需要坐标时，任何非零余式都拒绝；
随后还以完整原生矩阵乘法检查全部坐标的 $CH=A$。

原投影子算法仍按所有商坐标构造同一完整 suffix、所有原单项式及
乘基参数闭性。保留
$$
H=C I+H(1-e),
$$
包括每条原 generator 的正向包含、原幂等元等式、全商长度、
全部非约化重数、每个实际 residue map、全部原 closed point 和后继
四交、whole Norm、完整18×9 shadow门。只将原式中的多项式行运算、
稀疏左乘和 $C I$ 的计算换为上述忠实表示。

未知支持域走原完整实现；不把失败转换成抽样或删列。
所有原 source SHA pin 保留，投影子正文只有一处确切替换：
完整 $C I$ 的乘法调用，等式本身保留。

## 3. 一次公开软件核对

[公开入口](../scripts/check-original-complete-quadratic-api.py)
在29及41的完整二次域中，对含非素域对角系数和非约化幂的
upper Hermite 模块，与未修改原实现逐项比较全部余式、全部坐标及回乘；
还要求一个实际不包含的行被拒绝，核零行矩阵的原形状，
并作一次306列、完整长度612的指定软件样例。
这些样例不声称是原曲线的几何块。

[原生源](../scripts/original_complete_quadratic_polynomials.pyx)、
[接线源](../scripts/original_complete_quadratic_returns.py)；
标准接口参考 [FLINT nmod_poly](https://flintlib.org/doc/nmod_poly.html)。
数学执行只在公开 Actions，容器源目录只读且禁网。
不保存矩阵、系数、日志或可重算输出。回执完成后立即在本页登记，
再接回同一原完整几何作业；不原样重启未改进的 v11。


## 4. 首次实际回执与标量行的表示费用

run **46031932492**、job **140617645118**、source
**cf6a7d6a01952927919858a50c9819e2d9196231** 于16:15:48UTC返回 PASS。
两种完整二次域均逐项通过原余式/坐标比较、真实非包含拒绝和零行形状；
306列样例全回乘通过。总14.595466319s，306列样例三次操作10.391304137s。

- 原生源：14690B，SHA256 f8e7102dd4cca5090a14ff1ddf651bdfbc284d6e804d9274027eaed466eae52f。
- 接线源：4914B，SHA256 0d53aa812a716094de93d14a074ffe49dcd8c33ad8d8048b1e5e902aec5a3ed1。
- 核对源：5025B，SHA256 281658a8eadd606ab53781bcd5cd4bc450fffd4e714add766bdd8baad4cb618b。
- 完整结果 payload SHA256 b4fabf84dcd276029e3a8d9bd36a631be647f438b930ea9cfd6184d1d228af1e。
- 已读job log20984B，SHA256 c3f80deaeabe801ed55c18ade57b59d973ebfcea28b56a962d49893083f529b8。

306列费用说明不能在每个单行reduce中反复重编码整个基。后继只在同一
进程中暂存至多四份**完整**原生矩阵及其不可变完整副本；每次用前检查
原对象身份及当前全部矩阵与副本相等，原基一改即完整重建。
这是运算中的内存表示，不写文件、不跨run复用。新增一次实际修改基的
拒旧检查和八次单行使用的计时，专门验证这一具体风险；原全部数学门不变。

### 4.1 固定Sage10.6复制接口修正

后继run46032541530/job140619700531/source392591048656cb5f0c8aa779fe163c4eed912427于16:19:44UTC在首次缓存构造因Matrix_polynomial_dense没有.copy方法退出；未发生数学断言失败，也未产生PASS。已将接线与修改基核对中的复制改为Python标准copy.copy，保全部旧检查与完整相等检验。已读失败log SHA256 b2846b72a8aaeaa6fa23e5d0efc50f2f7e17d71e3f57a4f7a396d5fa57f4c51f。该修正随原公开入口执行，不修改原几何门。

## 5. 完整表示后继的实际PASS及接回唯一原作业

修正后run **46032975863**、job **140621181486**、source **5df58ad8ff1fbdaadc08c5a43de8c76786ef5025** 于16:23:04UTC真PASS。两原完整对照及非包含拒绝、实际修改基后的重建、306列/长612全部回乘均过；八次单行完整返回合计0.989544041s。表示命中26次、完整重建7次，总21.174297423s。这是软件样例的实值，不据此预测原几何整个时长。

- 原生源SHA256：7742254770d03bbdab649902e4a9faf92dc7e82c0fb360d279b496b7eb7ed917。
- 接线源SHA256：7da06cd12f35f7f2b98bf0c2c247c2732c838924c5497d3b8755b34932ce6d09。
- 核对源SHA256：07e6e0ee4c1c5bbca7ff5eef511de406d32fe8665fb630f10bb9cf12586018f6。
- 4873B结果payload SHA256：8a6d70354e07b1a19781b75917ed45f18f554f4a392becb5bb4b693551c45b5c。
- 已读完整job log27568B SHA256：cb7e8b91834f9d5c518cfb832405e4e0836a1f8ab6fddfe6d67098a08d8ced42。

后继v12将此两个已付源的实际hash固定后，接到未改正文的native v11生产器。原两char0 PASS pins、29/2453/64/minimal、API preflight=false及全部原门不变。host全60源manifest、源目录只读、Sage禁网和令牌仅host公共PASS读取保持；不装入任何旧矩阵或输出数据。唯一原重作业请求已提交，实际run回执后登记；尚未称四交/whole Norm/18×9影子完成。

### 5.1 原完整v12实际启动

实际run **46033409751**、job **140622660136**、source **048e20343a5f7ec65db9089d824d0635d6815b2b**；checkout与固定Sage镜像均成功，原两PASS认证及数学步骤于16:25:38UTC开始，读取时仍为in_progress。16:29所取早期job log为404 BlobNotFound，未取得数学输出，不作为数学成功或失败。继续同一个作业，不重复启动。
