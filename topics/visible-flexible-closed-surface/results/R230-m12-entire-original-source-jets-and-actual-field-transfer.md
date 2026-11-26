# R230：原 M12 整半图的连续源二 jets 与原微区间观察

2026-11-26，Astra-visible-flex-6a65e705-20261126 / g5-and-exact。

**完整引理与实际回执。** 原 R21 common-cut 图在整个活动半图上的
目标标架坐标二 jets 满足 $C_X<4461.108$。其中前缀、精确桥、
M64 common-cut 修正、全部 18552 个原尾多项式微区间、真实 deep collar
均已计入；24 个原 blob 的实际整流与有理预算 exit 0。
这是原位置图的连续界，不是新解的曲率采样。
它与 R226 的实际保存场六 jets 组成下面的全时几何传递充分条件。
本记录没有声称已消失的 CI 场已通过这些条件。

## 1. 对象、坐标与唯一源

记 $X$ 为 [R21](../results/R21-m12-whole-map-and-actual-metric-decrease.md)
的原精确 common-cut M12 图；目标 $g$ 保持原定义。
在活动半图的真实物理弧长和均匀材料角中，
$g=ds^2+f(s)^2du^2$，定义

$$
C_X=\sup\left(|X_{ss}|+\frac{2|X_{su}|}{f}
                     +\frac{|X_{uu}|}{f^2}\right). \tag{1}
$$

该范围从中央曲线一直到真实平圆领；$r=.6$ 是内部接口。
帽不参与后述修正，继续使用原已付曲率、支撑和标记结论。

原前缀 gzip 的 SHA256 为
359d491cd592962d467fdd538013977ee9a92070346de41c227d9ca3e1ef3bd0；
原 common metadata 为 253179d585d4ac0e59206d4e579de5663943f126473668c45a3bbda665c9c8f2；
精确桥证书为 1389cf1a339b0a0d749beb666b6def24a31e766eff0abf63289217728ceacdaa；
原尾 manifest 为 cc23977e25a09c34db91723dd784cab4b18b89e325fc2ca2fb8dd7ee6866a104。
后述程序逐一核这些身份。

前缀 raw 数据共有 2570 个节点、2569 个 quintic Hermite 微区间，
原 Fourier 阶为 M24。真正 common-cut 使用全部 M64 模。
尾的 24 个 gzip 共 18552 个微区间，复平面频数为
$-191,-188,\ldots,190$，竖直 cosine 频数为 $0,3,\ldots,36$。
原 manifest 里显示的累计 $r$ 和节点位置只是数值显示；
严格的源使用准确正增量 $\ell_i$、准确归一化 $\beta$ 和
$r_i=r_{\rm in}+\beta\sum_{j<i}\ell_j$。
本程序不把那些显示位置当精确插值节点。

## 2. 原尾每个完整微区间的 Bernstein 证书

令 $L=\beta\ell_i>0$，局部变量 $t=(r-r_i)/L$。
对任一个实 Fourier 系数，记准确起值为 $v$，
$F_r$ 的两端值为 $f_0,f_1$，两端导数为 $s_0,s_1$，
中点值为 $m$。原定义的 quartic $F_r$ 的五个 Bernstein 控制数恰为

$$
b_0=f_0,\quad b_1=f_0+Ls_0/4,\quad
b_2=\frac{16m-5(f_0+f_1)-L(s_0-s_1)}6,\quad
b_3=f_1-Ls_1/4,\quad b_4=f_1. \tag{2}
$$

前三个插值条件和两个端导数条件确定这一个 quartic。
把 (2) 展开到幂基即可逐项核对原 integrated-quartic 定义。
其积分 $F$ 的 quintic 控制数是

$$
p_0=v,\qquad p_{j+1}=p_j+Lb_j/5,\quad 0\le j<5, \tag{3}
$$

而 $F_{rr}$ 的 cubic 控制数为
$4(b_{j+1}-b_j)/L$。特别地

$$
F(r_{i+1})-F(r_i)
=\frac{L[7(f_0+f_1)+16m]}{30}
 +\frac{L^2(s_0-s_1)}{60}. \tag{4}
$$

程序以准确 Fraction 累积 (4)，所以相邻值、Fr、Frr 真的共享；
它没有对量化累计位置作有限差分。
所有 Bernstein 基函数在 $[0,1]$ 非负且和为一，
故控制数绝对值最大值控制完整微区间。
对完整 Cartesian 复频数 $m$ 用 $|m|^j$，
对高度 cosine 频数 $n$ 用 $|n|^j$，求系数绝对和即给
$V,V_r,V_u,V_{rr},V_{ru},V_{uu}$ 的全角界。
此处平面频数已经包含旋转标架，不能再把它当 $3k$。

在 $[r_{\rm cuff},r_{\rm in}]$，使用原准确 quintic collar。
若内侧要求三迹 $a_0,a_1,a_2$，其幂系数为

$$
P(t)=(10a_0-4ha_1+h^2a_2/2)t^3
 +(-15a_0+7ha_1-h^2a_2)t^4
 +(6a_0-3ha_1+h^2a_2/2)t^5, \tag{5}
$$

其中 $h=r_{\rm in}-r_{\rm cuff}$。同一 Bernstein 算法覆盖整个
collar，且 cuff 的两 jets 精确为零。旋转背景仍为原解析无限尾；
本证书没有把第 160 层以下的背景改成有限数值高度。

写原尾 $X=\overline X+V$。复用已经证明的整个原背景
$|\kappa_r|\le6$，而不是把它当改后实际曲率。
令 $E=1+w^2$，物理增 $s$ 方向指向内半径，则

$$
r_s=-E^{-1/2},\qquad r_{ss}=-ww_r/E^2.
$$

因此 $|r_s|\le1,\ |r_{ss}|\le6$，并且
$|\overline X_{ss}|\le6,\ |\overline X_{su}|\le1,\
|\overline X_{uu}|=r$。在一个微区间 $r\ge r_0>0$ 上，

$$
C_X\le6+\frac3{r_0}
+B_{rr}+6B_r+\frac{2B_{ru}}{r_0}+\frac{B_{uu}}{r_0^2}. \tag{6}
$$

这是实际坐标二 jets 的界；没有把近似图的第二基本形式换成背景第二基本形式。

实际完成的全部微区间给

| 完整原尾项 | 向外保守上界 |
|---|---:|
| $|V|$ | $0.000974143$ |
| $|V_r|$ | $0.013363862$ |
| $|V_u|$ | $0.002866114$ |
| $|V_{rr}|$ | $5.028731$ |
| $|V_{ru}|$ | $0.039466637$ |
| $|V_{uu}|$ | $0.008792054$ |
| 式 (6) 对全部有限尾和真实 collar 的最大值 | $26.000001$ |

式 (6) 的最坏保守值出现在 deep collar 的内半径端：
$6+3/r_{\rm cuff}$ 略大于 26，因为原准确 cuff 是
$2702159776422297/18014398509481984$。
不能把 binary64 显示 26.000000000000004 改写成严格 $C_X\le26$。

逐有理行流 SHA256 为
965d7c04d888679baf436b68c6ff31c8744d882cfcd0457ceeb9d51920959eda。
它覆盖全部 18553 个有限/领微区间，每行包含准确端点、六项界及 (6)；
没有用有限径向采样代替连续范围。

## 3. 完整 prefix、准确 bridge 与 M64 接头

原前缀每个 quintic 的幂系数来自准确二进制节点 two-jets；
均值高度差使用准确 mean_increment。
角导数杀掉常数高度，所以求 (1) 不需用近似累计高度。
程序对 2569 个完整微区间逐项转成 Bernstein 控制数，
不是只取首 ramp 或 73 个旧补丁微区间。

M64 common-cut 接头由同一整流得到的准确尾端点决定。
位置端值使用 cache 的完整 numerator/denominator；Fr/Frr 端迹则是
原末尾 blob 的 binary64 列直接 copy，原定义本来就是这些准确 dyadic。
它们不是把算出的有理端导转回 float：streamer 从 little-endian f64
原数组取 values[-1,1]、values[-1,2]，不作运算，原 dtype 一并存入 cache。
归一化只进入式 (2) 的实际长度 $L=\beta\ell_i$；两端 physical-r 导数
仍恰等这两个 dyadic 输入。因此接头程序的 fq(float64) 没有丢弃有理余项。
以 $\lambda$ 的原精确区间保留准确桥尺度，
以有理平方根包住 $k=-2/\sqrt5$，并保留准确恒等式 $k^2=4/5$。
原尾高度的镜像符号与高度 gauge 与 CommonCutSource 完全相同。
若 native 接头宽度为 $h$、右端三迹差为 $\Delta_0,\Delta_1,\Delta_2$，
其完整 quintic 修正的三阶控制预算为

$$
\begin{pmatrix}B_0\\B_1\\B_2\end{pmatrix}
\le
\begin{pmatrix}
1&2h/5&h^2/20\\
5/h&2&h/4\\
20/h^2&12/h&2
\end{pmatrix}
\begin{pmatrix}|\Delta_0|\\|\Delta_1|\\|\Delta_2|\end{pmatrix}. \tag{7}
$$

这是分别对三种 Hermite 基的 Bernstein 控制数取绝对界；
并未把完整端口的 $X_{ss}$ 删除。

材料角仍为 $u=\psi-e(s)\sin(3\psi)/3$。
本次覆盖原 clamped cubic 的全部 64 个片，
并在准确 $x=3/4$ 再切一次，共 65 片。
在 $x>3/4$ 乘完整 quintic cutoff，连同其一、二阶乘积项一起计算。
程序对每个最高八次的乘积多项式作准确 Bernstein 界，得到

$$
|e|<.800001,\quad |e_s|<1.156887,\quad |e_{ss}|<6.953008. \tag{8}
$$

正式链式法则使用未截断 Fraction，不使用 (8) 的显示截断。
置 $\rho=1-E_0>0$、$A=E_1/(3\rho)$，使用 R216 已给的隐式角图公式

$$
C_{ss}=\frac{E_2/3+2E_1A+3E_0A^2}{\rho},\quad
C_{su}=\frac{E_1+3E_0A}{\rho^2},\quad
C_{uu}=\frac{3E_0}{\rho^3}.
$$

若完整 native Cartesian 二 jets 的界为
$B_\psi,B_{ss},B_{s\psi},B_{\psi\psi}$，则

$$
H_{ss}=B_{ss}+2AB_{s\psi}+A^2B_{\psi\psi}+C_{ss}B_\psi,
$$
$$
H_{su}=(B_{s\psi}+AB_{\psi\psi})/\rho+C_{su}B_\psi,\qquad
H_{uu}=B_{\psi\psi}/\rho^2+C_{uu}B_\psi. \tag{9}
$$

这里水平 Fourier 权重是 $3j+1$，高度权重是 $3j$，
所以圆柱标架的角导数已付清。

整个上/下 ramp 的目标半径至少为 1。
准确 bridge 的
$\phi=t^2[p_t(3-2t)-Lp_s(1-t)]$ 满足 $\phi\ge0$，
因为 $p_t,L>0,p_s<0$。
用精确 $L,p_t,p_s$ 区间作 64 个完整 cubic Bernstein 片，
实际证明 $\phi<1.335373<3/2<\pi/2$。
故 $f'=-\sin\phi\le0$；原精确根条件 $f(L)=c$ 给整个 prefix
$f\ge c=5404319552844595/9007199254740992$。
这个全域半径下界没有借用只覆盖旧字段支撑的 R114 结论。

由 native 到物理 $s$ 的尺度为原准确 $\lambda$，最终

$$
C_{X,\mathrm{prefix}}
\le \lambda_+^2H_{ss}
 +\frac{2\lambda_+H_{su}}c+\frac{H_{uu}}{c^2}
<4461.108. \tag{10}
$$

完整 native 原项的保守上界分别为
$2.601650,5.765739,2.361363,7.412301$；
完整 M64 接头增加项分别小于
$4.511\cdot10^{-9},9.851\cdot10^{-8},
1.508\cdot10^{-7},5.495\cdot10^{-7}$。
接头三迹虽小，程序确实逐项纳入了 (10)。

前缀逐微区间有理行流 SHA256：
75320338af08c429dc7d9e6eff85a79f4d6f7e5f8d9c4c13a49c40000ad45d80。
完整角图逐片行流 SHA256：
de1fae697e46f9ecdb905c5c31ad30803a31568b7e999d6d1f92b743e1377aaf。
结合 (6)，式 (1) 在整个原活动半图满足 $C_X<4461.108$。

## 4. 真实保存场的几何消费条件

令 $Y=X+C+W$，其中 $C$ 是
[R226](../results/R226-m12-normalized-reference-and-continuous-cartesian-bounds.md)
的确定中央归一化修正，$W$ 是同一次 whole solve 保存的实际 B-spline 场。
中央精确周长归一化、准确桥尺度差、原 mean-height gauge 都已经包含在 $C$；
不能只把保存的 learned coefficients 当成 $Y-X$。

R226 checker 从真实 knots/coefficients 给完整六 jets 连续界，
并用原 R223 公共图把单位 $z$ 和中央 $\theta$ 转为物理 $s$、均匀 $u$。
其报告已经利用 $C$ 支撑处 $f\ge1$、
全半图 $f\ge r_{\rm cuff}$，给

$$
\eta\ge|C+W|,\quad p\ge\|d(C+W)\|_{g,F},\quad
C_W\ge|(C+W)_{ss}|+2|(C+W)_{su}|/f+|(C+W)_{uu}|/f^2.
$$

为明确充分条件，取原
$d=2.57212\cdot10^{-8}$、
$K_0=4763997235009095/562949953421312$、
$R=2131902881202937/1125899906842624$，定义

$$
d'=d+2(1+d)p+p^2,\qquad
\epsilon_n=\frac{3p+p^2}{1-d},\qquad
K'=\frac{K_0(1+d)+\epsilon_n C_X+C_W}{1-d'}. \tag{11}
$$

当 $d'<1$ 时，(11) 对整个同伦 $X+\tau(C+W)$ 有效。
它沿用 R216 的真实法向差和实际第二基本形式恒等式，
没有以背景曲率替代新曲率。新支撑和包围半径满足

$$
h'>.737-1.9\epsilon_n-\eta,\qquad R'<R+\eta. \tag{12}
$$

若 $h'>1/K'$，R10 的正支撑全局管结论作用于这个真实闭 C² 浸入，
给嵌入和 reach 至少 $1/K'$。因此

$$
\frac{\operatorname{reach}}{D'}\ge\frac1{2K'(R+\eta)},\quad
\frac{\delta_{\rm hold}}{D'}>
 \frac{.19989114-2\eta}{2(R+\eta)},\quad
\frac{\operatorname{diam}H}{D'}>
 \frac{3.5426}{2(R+\eta)}. \tag{13}
$$

可执行 consumer 对实际 result/field/grid 与 source cache/report 逐一核 SHA，
并把未通过的保守不等式记为 unresolved。
它不把“脚本 exit 0”改写成这些条件已经通过。
基础比例阈值与更尖的旧显示阈值分开列出；
更尖阈值未过不自动宣称该新图失败。

## 5. D3、含反射非全等与全时间

保存的真正 basis 是实系数
$\sum a_m(s)e^{im\theta}$，$m\in1+3\mathbb Z$，
以及实系数 $\sum b_j(s)\cos(3j\theta)$。
R226 checker 核对实际 mode arrays，不能用另一个假定对称的基代替。
原中央曲线的速度 $J(\theta)$ 为偶函数且 $2\pi/3$ 周期。
准确弧长角 $U_0(\theta)=a^{-1}\int_0^\theta J$ 因而满足

$$
U_0(-\theta)=-U_0(\theta),\qquad
U_0(\theta+2\pi/3)=U_0(\theta)+2\pi/3.
$$

其逆图保持相同性质。故实际 $W$ 在均匀材料 $u$ 下保持 D3 和
$y\mapsto-y$ 镜像；原图与确定中央修正 $C$ 也如此。
新活动体的三阶复体积矩 $A_3'$ 为实数。

若 (11)–(12) 的整个同伦已付、$\eta<1/K_0$ 且 $R+\eta<2$，
复用 R216/R16 的原法向管和面积小于 150 的预算，

$$
|A_3'-A_3|\le2400\eta(1+9\eta)^2. \tag{14}
$$

若右边小于 $.44016$，则 $A_3'>0$。
固定帽标记仍是同一个 $B_3>0$，并要求新管包含其高度 $1/2000$
（consumer 明确检查 $K'<2000$）。
R16 的中心三阶张量范数差仍为 $A_3'B_3>0$。
该范数对整个 $E(3)$ 不变，包括反射；
紧性论证于是给真正的 $\delta_E>0$。
这里没有推出 $\delta_E/D'\ge5\%$。

完整相位族是 $Y_\alpha=R_\alpha Y\circ\tau_{-\alpha}$，
按原下半镜像和完整固定帽规则接合。
$g$ 对 $\tau_\alpha$ 不变；中央/真实 cuff 的修正两 jets 精确为零，
故每个相位的 C² 接口和固定帽都保持。
(11)–(14) 在空间旋转下不变，给全部连续相位，
不是有限时刻抽样。

## 6. 第 190 个 whole 元里的原微区间观察

公开首个 whole CI 的 G6 训练峰索引 1141、G8 独立峰索引 1522，
都属于零起算第 190 元。
按相同原 FrozenSource 数值重建，该元两端公共坐标是

$$
q\approx2.2018730911292757,\qquad
q\approx2.204588395105453,
$$

宽约 $.00271530397617736$。
左端是原解析 cell $n=0,j=3$ 的右半径端；
右端是第 26 个均匀尾 knot。
该元 G8 第三点正是原独立峰 $q=2.2025172529962367$。
以上是数值位置辨认，不是区间证书。

本次准确整流在 $r\in[.432,.436]$ 相交的 74 个原源微区间中
加入全部端点及四分点，共 297 个不同准确半径。
每个点先经 R223 逆回同一 $q$，再在该 $q$ 求同一 Cartesian basis；
两部分的 jets 都是物理 $s$、中央 $\theta$，并使用同一目标 Gram。
数值逆回半径最大误差为 $1.404\cdot10^{-16}$。

本地实际运行的是明确标注 reference-only 的接口验证，
未使用、未假称恢复旧 CI 的 learned field。
N768 得原参考峰 $1.9672081297272825\cdot10^{-8}$，
位于 $q\approx2.2023120352036494$、
$r\approx.43501355623459441778$、原全局 source span 17149，
仍为 whole 第 190 元。
它比旧 G8 独立参考峰 $8.75957\cdot10^{-9}$ 高约 2.25 倍；
附近还有另一窄起伏。故更密原微区间观察是实际需要，
并不能把旧 G8 最大值当连续最大值。

新 cold 入口会把同样的观察用于同 job 实际保存的 learned field；
它不会把 reference-only 的 before=after 包装成求解改善。

## 7. 实际执行、源码与再生

旧环境丢失前两份尚未推送的尾预算文本无法逐字复原，
故本次明确另用 recovered 文件名和新 SHA。
没有沿用旧未登记源码的执行身份。

| 源码 | SHA256 |
|---|---|
| 6a65-m12-tail-polynomial-continuous-bounds-recovered.py | be6f687af2a0056145aad60737dac613f3d79680aec7ec2cdafb584dda1d6e72 |
| 6a65-m12-stream-tail-query-and-source-bounds-recovered.py | f890c445f635713c70db43446c67f8825baf457a2c9c17c0c770c296acad278b |
| 6a65-m12-original-common-cut-prefix-source-bounds.py | b71e1b7bd0c02a19d047793574afcf49e41a2378435f73e7cf56efef65f8a9d3 |
| 6a65-m12-entire-half-actual-field-geometry-transfer.py | d6e31c7be1b700a0a6d5ef33048ce2376229de421c9afde64670cc6c367f46b6 |
| 6a65-m12-entire-half-original-span-observer.py | 2bd23a49bcfe06d05f6a22dc1dd744161428bfbbbe27a24cc902638e1eb8b0d2 |
| 6a65-m12-entire-half-cold-with-continuous-budgets.py | 6c92f75e752d5c581b7642a576905c3c6fa436a174a8f4ff711e38d862a98136 |

六源码实际 py_compile exit 0。式 (2)–(3) 与原幂基的
60 个 Fraction 身份检查全部相等；通用证明仍由 (2)–(4) 给出。
随后不是只停在代数自检，而是实际消费全部24blob。

实际本地全尾请求仅三枚基础端点及上面的诊断窗口，
查询清单就是准确 $r_{\rm cuff},r_{\rm in},c$ 的 Fraction 字符串。
可用以下完整命令重生；所有输出放临时目录。

~~~sh
python scripts/6a65-m12-stream-tail-query-and-source-bounds-recovered.py \
  --manifest notes/2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json \
  --endpoint-producer scripts/6a65-m12-stream-tail-exact-endpoint.py \
  --queries /tmp/m12-source-cx/three-source-endpoints.json \
  --out /tmp/m12-source-cx/original-source-tail-cx-and-local-spans.json \
  --source-transport raw-known-commit \
  --diagnostic-window .432 .436 --diagnostic-subdivisions 4
python scripts/6a65-m12-original-common-cut-prefix-source-bounds.py \
  --scripts scripts --data /tmp/m12-source-cx/m12-prefix-data.npz.gz \
  --tail-report /tmp/m12-source-cx/original-source-tail-cx-and-local-spans.json \
  --tail-cache /tmp/m12-source-cx/original-source-tail-cx-and-local-spans.json.npz \
  --out /tmp/m12-source-cx/original-entire-half-source-CX.json
~~~

原始24文件从已知历史提交
aed993f7bd33fc6f545f941171c1b78d67258cca 的公开 raw 路径读取，
每个仍严格核 manifest bytes、SHA256 和 Git blob framing SHA1。
API 模式也保留，Actions 仅以 github.token 读已知公开 blob。
令牌不写源文件、输出或提交；非恢复子进程剥除 M12_RECOVERY_TOKEN。

实际全尾 exit 0，711.881763933 秒，HWM64656KiB；
source report SHA256
2c62cfbee09b36cd615e906cbaf238984a8171bc43a912afdcfd8e8d3bd4802a，
其临时 numerical cache SHA256
6c16f10158f1cceb321d40f3a2eb7c300e9064bf233df0fc772bc2dae842fba8。
前缀/整半图源预算 exit 0，37.014825115 秒，
report SHA256 f63d8e2db5c94c77bde7bf0835a6f8f62b1ebf1b6d35687db3ac59108bb453f8。
reference-only 微区间观察 exit 0，63.921540226 秒，
report SHA256 4fed70299db0ef450f04c7227e092a683d1e8d5366fd81fe2e9adf0b2b020407。

这些 JSON/cache 是可再生输出，只保临时目录；
提交对象为小源码、本文和必要标量回执，不能上传 raw artifact/release。
下一同配置 whole run 的单一入口为：

~~~sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
  topics/visible-flexible-closed-surface/scripts/6a65-m12-entire-half-cold-with-continuous-budgets.py \
  --scripts topics/visible-flexible-closed-surface/scripts \
  --data /tmp/m12-source-cx/m12-prefix-data.npz.gz \
  --directory /tmp/m12-source-cx/whole-budgeted \
  --prefix-elements 80 --tail-elements 64 --tail-depth 12 \
  --order 32 --angular 384 --gauss 6 --iterations 800 --newton 1 --block 24
~~~

该入口依次执行七阶段：prepare、准确尾查询和连续尾界、完整前缀/整半图源界、
原 whole solve、R226 实际保存场六 jets、实际场全时几何传递、原微区间观察。
保持原离散求解配置，新的输出用于核连续预算和观察盲区；重生本身不计新的数学下降。
五份供 caller 读取的小标量 JSON 分别为 entire-half-original-source-bounds.json、
entire-half-result.json、entire-half-continuous-change-bounds.json、
entire-half-actual-field-geometry.json、entire-half-original-span-observer.json。
raw field/cache/点数组只留同 job 临时目录；统一 receipt 对各文件记录 SHA。
新 cold 入口的完整 whole solve 与实际保存场传递须等各阶段自己的真实回执。
本引理支付原图连续源预算，尚未支付精确等距、固定 g 的无限细化极限、
20% held 或 5% Euclidean 非全等幅度。

