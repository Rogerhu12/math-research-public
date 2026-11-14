# 完整160格真实非线性尾：深层组合算术入口

2026-11-12，numerical_recovery。状态：**实现与有限数值证据**。
这里不声明无限尾、完整强目标曲面或收敛的非线性 DN。

## 1. 实际恢复与先前退出

07:47附近执行器实际报告 `executor key changed during session recovery`。
旧未推的05/06/07输出实体已丢；旧07真实退出未知。
从Git恢复的可靠非线性起点仍是旧tail04的第三响应，其物理尾与这里的新尾不同。
未把历史观察中的已丢向量补造成新实体。

本次物理输入为
`2026-11-12-fd2d-layered64-wc01-recovery02-config.json`，SHA256
`d4d41047c5afa1df90e17e3814e896a7cd91f64c79d0e11116e071cb97e17994`。
cut/cuff为.50/.32，wc=.1，前160格的β与pulse/valley caps均真实校准。
0…159全部进入非线性射击；160之后保留原source。
当前有限线性外端在196，仍是有限Robin近似，不写成原无限尾通过。

`numerical-gc-layered64-full160-01` 实际启动后，Node明确原生heap OOM，
returncode −6；driver正常记录并exit0。
在ready前失败，无完整F、响应或accepted。实际heap128MiB。
它已完成2880个线性stage图，但当时heap_used为107163544B。
完整关闭报告、stderr、输入、源快照已交root发布。

新的point cache为每entry8项。每个物理格只建立实际使用的root/split/product引擎；
旧legacy raw引擎只在显式请求legacy诊断时分配。
这两项只改变存储；modified source、方程、floor与求解容差未变。

## 2. 具体下溢与准确组合式

实际source最深谷在raw159/seg3/x=1：

$$
r=.32,\quad r_x=5.836462807474886\,10^{-76},\quad
\log w=-423.7456058685332,\quad w=9.324415992003524\,10^{-185}.
$$

binary64中先算$w^2$给0，不能据此拒绝正的物理$w$。
记$\mu>0$为本格固定canonical归一化，$o=\pm1$，
$\sigma=r_x/r$，$\Lambda=\log\mu-2\log w$。
原根/动量/角导数因子准确为

$$
T={o\sqrt6\mu\over r^4w^2},\quad I={or^4w^2\over\sqrt6\mu},\quad
P={or^3r_xw^2\over\sqrt6\mu},\quad C={r^3\over\sqrt2w}.
$$

新入口在$\log w<-250$时先合并这些幂的对数再取exp；正常区间保持原运算次序。
特别有准确恒等式

$$
PT=\sigma,\qquad PC={or^6r_xw\over\sqrt{12}\mu}.
$$

这里$P$为通量因子，角向场在源码中仍沿用`v.P`名称；两者不能混淆。
若$K,L,p,p_\theta$为角向无量纲场，原判别式中的组合改写成

$$
u=2w(wK)+(wK)^2+(1+w^2)(wp)^2,\quad
S=1-(wp)^2,\quad A=1+L+w(wp_\theta).
$$

相同重排用于root Gram/JVP、split非线性通量、几何Newton retraction。
不是把含$w^2$的项删为0；先乘$w$再平方保留能够表示的组合。
原完整均值root、30次上限、$8\,10^{-14}$阈值、原roundoff fallback及floor .05保持。

## 3. Fourier-product解析JVP的缩放

原product代码求的是$dL_{corr}=dL-T\,d\pi$，
不是完整$dL$；这是其线性部分已经单独精确投影的缘故。
设原Gram为$B$。新的deep分支直接解

$$
B\,D=P\,(\text{原右端}),\qquad D=P\,dL_{corr}.
$$

$d\pi$列用$PT=\sigma$；$dQ$列用上述$PC$。
输出Jacobian需要的其余准确组合为

$$
R={o\sqrt{12}\mu\over r^7w},\quad
A_\pi={o\sqrt{12}\mu r_x\over r^8w},\quad
Z={o\sqrt6\mu\over r^3w}.
$$

于是Q行的非线性项为$R D_j$，线性$\pi_j$项为$A_\pi$；
均值高度行是$ZD_0$。
动量行直接用已经乘$P$的通量差分，避免先造巨大的$dL_{corr}$再乘趋零$P$。
全部Fourier乘积矩、基频和投影数仍沿用原实现。

## 4. 实际两jet与audit

metric代理闭存
`scripts/fd2d-metric-deep-momentum-physical-jets.mjs`，SHA256
`c1edc34d514d661b9282a9715b603ed4d436acf3708244a11c455be999b6a5d3`。
它消费本入口`rhsWithComponents`给出的真实完整未乘pref动量通量。
隐式根时间导数的原项准确改写为

$$
T[\dot\pi_j-(4\sigma+2k)\pi_j]
=\sigma m_j\,\mathrm{flux}_j-2k(T\pi_j),\quad k=(\log w)_x.
$$

同时$\dot p_j=((m_j^2-1)\sigma-k)p_j-m_j\sigma L_j$。
实际physical二jet仍由同一有限root和实际ODE求得，未用另一个形式系统替代。
每角另外返回`normalizedDarboux=A*b-G`；core audit直接使用它，
不再通过`physicalDarboux/w²`产生0/0。
物理Darboux若本身小于binary64最小数，明确计入underflow count；
没有把这个0误作归一化缺陷准确为0。

## 5. 已实际执行的局部核对

第一个checker启动在import处实际exit1（chunk65b466），
因为只读dependency列表没有包含旧fast-split附加源；尚未运行数值fixture。
v2使用原运行快照中真实旧路径，与原worker的导入方式一致；失败receipt保留。

v2实际session57472，launch97a30a，completion59525b，exit0，4.34秒。
报告`2026-11-12-fd2d-numerical-gc-deep-arithmetic-check-02.json`与receipt已保存。

正常点的10个state、5个root、10个RHS、80个Jacobian、5个Ldot值
与旧冻结实现逐位相同。
实际raw159最深谷在$w^2=0$下，root/RHS/Jacobian/physical两jet全部有限；
minA=.9971725728747538、minD=1，root相对残差$4.236\,10^{-19}$。
归一化Darboux非零，峰$3.615\,10^{-88}$；64角physical值下溢明确记录。

同一点把$w$乘一个常数、$\mu$乘其平方，Q/高度乘同一常数，
得到普通数值范围的对照：normalized root最大绝对差$1.137\,10^{-16}$，
Jacobian按对应坐标换回后最大绝对差$2.205\,10^{-38}$，
Ldot最大绝对差$6.520\,10^{-91}$。
逐分量相对误差对几乎为零的对称高模会较大，报告保留该原值，不隐藏。
这些都是具体局部算术核对，不是新强几何证明或额外完整尾验收。

## 6. 第二次真实完整请求

独立运行目录：`/workspace/scratch/fd2dbfd2c83e/visible-flex-gc-layered64-nonlinear-02`。
session78644，launch de6b10；worker
`scripts/fd2d-gc-tail-partition-worker-v6.mjs`。
真实请求REAL cosine height为$[-10^{-9},0,0,0]$，无需额外$\sqrt2$。
M4/N64、physicalDepth160、far196、parts2、steps32、linearSteps256、tol2e−9。

08:19:25 UTC启动，实际heap167772160B；08:19:47全部2880线性stage图完成，
heap_used50502184B/RSS122302464B，已经真实ready并保存请求初猜。
初猜gzip32881B，SHA256
`c1bc7769e12354d40af1b0192f8e4f6ca830100f42c2e67e7fdb01597f9babc1`。
08:20:21完整F/J已实际缓存1920/2880段；当刻没有完整norm或accepted，
不能据此写DN成功。

静态config/request/source-input-manifest/runtime-source-snapshot已复制到notes，
共同stem `2026-11-12-fd2d-numerical-gc-layered64-full160-02`。
活动输出仍在独立树；后续真实终止时闭存并更新本节，不由无输出推断退出。
root继续前缀幅度/外层设计；本代理独占当前真实nonlinear DN。

## 7. 02真实接受与物理raw试步量化；03继续

02随后完整完成2880全F/J，实际norm为.00760429776100453。
三个lambda1全F真accepted依次为
.0016237284101061752、.0016237283781537783、.0016237283781452912。
最后一个实际state gzip120577B，SHA256
`d5a6f1157ddf1c4ad5ae60e6f9ef0d8f530a9d31effd08de58c8f6218a68c854`。
其后iteration3又完整求得同一norm、minA=.9950578044371454、
minD=.9999999983990001；完整迭代实体另存，不能称2e−9已经达到。

误差峰为stage2640/raw146/seg2/component4，绝对
$5.030672849821754\,10^{-278}$，本格scale为$3.098223149593564\,10^{-275}$。
针对这一个真实已存stage做实际流与$J\cdot y$检查，session58122真exit0；
二者差相对初始state只有$6.217\,10^{-16}$。
报告`2026-11-12-fd2d-numerical-gc-deep-stage2640-01.json`完整记录，没有另做全尾求解。

此时$\log w\simeq-178.303$，$w^2$仍可表示。
问题出在旧R95试步把无量纲$L$先转成物理raw斜率

$$
q^{raw}_j={w\over\sqrt6r^3}L_j.
$$

这个数已接近binary64次正规数底部。真实局部方向$\delta\pi=10^{-278}$
被转成最小正数`5e−324`，其原centered试步的实际canonical增量为0。
并非原F/J算错，而是试步曲线的中间坐标把可表示的方向丢掉。

新`fd2d-gc-tail-normalized-retraction.mjs`直接取
$Q(\lambda)=Q+\lambda\delta Q$与非均值
$L(\lambda)=L+\lambda\delta L$，再解原完整均值root并转回canonical $\pi$。
固定物理节点的$w/(\sqrt6r^3)>0$是常数，因此这和旧raw直线是**准确相同的几何曲线**。
只略过中间的物理raw表示；均值root阈值、centering、原Newton方向、原F/J与接受规则不变。

真实局部check02，session14967（f81375→f54e12）exit0：
新实际canonical增量$1.0000000000000001\,10^{-278}$，相对方向误差
$1.566\,10^{-16}$；普通点新旧试步最大state差$1.010\,10^{-28}$。
初次checker过强地要求raw方向本身必须恰为0，实际它是5e−324，故该checker真实exit1；
完整失败记录保留，后一个checker报告实际量化值而没有重写前次结果。

保存完整accepted2与iteration3后，owner主动停止02：工具chunk744a0f实际exit130。
没有自然Node退出码可推断，不写外部kill或收敛成功。
9份关闭输出及完整manifest已在notes。

03实际session66020，launch782b49，08:29:50 UTC开始，独立目录
`/workspace/scratch/fd2dbfd2c83e/visible-flex-gc-layered64-nonlinear-03`。
v7仅换用上述normalized retraction，精确warm来自02 accepted2。
其余physical cfg、M4/N64、160/far196、parts2/steps32、floor/tol保持。
实际heap167772160B、pointcache8；本次更新时还在原完整线性图初始化，
不把未完成ready记作已得到响应。静态源/输入/快照已闭存notes，活动输出只在独立树。
