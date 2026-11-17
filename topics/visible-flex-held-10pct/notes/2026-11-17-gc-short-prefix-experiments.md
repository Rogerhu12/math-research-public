# Gauss–Codazzi 局部试算：未闭合的短前缀

会话：`literature_mechanisms`，2026-11-17。本文件记录数值证据；没有完整圆领、闭面、全程 reach 或 10% 解。

## 1. 方程核对（完整直接计算）

令 `s` 为经向弧长，`u` 周期 `2pi`，

$$g=ds^2+a(s)^2du^2,\qquad b=L\,ds^2+2M\,ds\,du+N\,du^2.$$

非零 Christoffel 符号只有

$$\Gamma^s_{uu}=-aa',\qquad\Gamma^u_{su}=\Gamma^u_{us}=a'/a.$$

曲率为 `K=-a''/a`，故 Gauss 式为

$$LN-M^2=-aa''.$$

从 `nabla_u b_ss=nabla_s b_us` 得

$$L_u-2(a'/a)M=M_s-(a'/a)M,$$

从 `nabla_s b_uu=nabla_u b_su` 得

$$N_s-2(a'/a)N=M_u-(a'/a)N+aa'L.$$

于是父会话的两条 Codazzi 公式完全正确：

$$M_s=L_u-(a'/a)M,\qquad N_s=M_u+(a'/a)N+aa'L.$$

当 `N` 非零时，可消去

$$L=(M^2-aa'')/N.$$

`(M,N)` 的主部矩阵是

$$A=\begin{pmatrix}2M/N&(aa''-M^2)/N^2\\1&0\end{pmatrix},$$

特征值为 `(M+-sqrt(aa''))/N`。所以 `a''>0` 对应负高斯曲率的双曲演化；`a''<0` 对应椭圆 Cauchy 延拓，高频误差会指数放大。

移动标架 `e1=F_s,e2=F_u/a,n=e1 cross e2` 满足

$$F_s=e_1,\quad (e_1)_s=Ln,\quad(e_2)_s=(M/a)n,$$

$$ (e_1)_u=a'e_2+Mn,\quad(e_2)_u=-a'e_1+(N/a)n.$$

脚本正是先谱计算 `M,N`，再同时积分前三条 `s` 向 ODE，并检查 `F_u-a e2`。

## 2. 椭圆等速初值与初始曲率代价

对 `A=1,B=.7` 的椭圆，令其按弧长等速参数化为 `gamma(u)`。则

$$a_0=\frac{\operatorname{perimeter}(\gamma)}{2\pi}=0.8566306289457476,$$

而不是 1。取 `F_s=e_z`，内法向 `n=e_z cross (gamma_u/a0)`，则

$$a'(0)=0,\quad M(0,u)=0,\quad N(0,u)=a_0^2\kappa(u),\quad
L(0,u)=-\frac{a''(0)}{a_0\kappa(u)}.$$

椭圆曲率范围为 `[.7,2.0408163265306127]`。若 `a''(0)=c>0`，

$$F(s,u)=\gamma(u)+s e_z+\frac{c s^2}{2a_0\kappa(u)}\nu_{\rm out}(u)+O(s^3).$$

因此在两条轴端，半径差的二阶变化为

$$A(s)-B(s)=A-B+\frac{cs^2}{2a_0}\left(\frac{B^2}{A}-\frac{A^2}{B}\right)+O(s^3).$$

括号为负，故负曲率的先外张阶段确实能使椭圆截面变圆。代价是初始经向主曲率绝对值最大 `|c|/(a0*kappa_min)`。必要的局部 reach 条件为

$$|c|\le\frac{a_0\kappa_{\min}}{0.03D}.$$

只用 `D>=2` 可得 `|c|<=9.9940240`；完整闭面的 `D` 可能更大，实际限值更小。

注意：`c!=0` 的起始段不能 `C2` 接一段直母线椭圆柱；要接柱段，必须令 `a''(0)=0`，本轮后续 ramped 试算已经做到。

## 3. 圆解附近的 Fourier 传递系统

在 `|a'|<1` 的旋转背景，写

$$w=\sqrt{1-a'^2},\quad L_0=-a''/w,\quad N_0=aw,\quad M_0=0.$$

对线性模式 `deltaN=n_k(s)cos(ku), deltaM=m_k(s)sin(ku)`，置

$$q=a'/a,\qquad c_*(s)=a''/(aw^2).$$

直接线性化得

$$m_k'=-q m_k-kc_*n_k,\qquad
n_k'=k m_k+(q+aa'c_*)n_k.$$

只要 `a,w` 都不为零且系数正则，这是可逆的二阶线性系统；非零模式在有限正则区间不能同时变成 `m_k=n_k=0`。其基本解矩阵的行列式满足

$$\det\Phi(s)=\det\Phi(0)\,\frac{w(0)}{w(s)}.$$

等价地，令 `xi=(w/a)n_k, beta=a m_k`，得到迹为零的 Hamilton 型系统

$$\xi'=\frac{k w}{a^2}\beta,\qquad
\beta'=-\frac{k a a''}{w^3}\xi,$$

即

$$\left(\frac{a^2}{w}\xi'\right)'+k^2\frac{aa''}{w^3}\xi=0.$$

自由选择 `a` 的作用是调节各角频的相位与增长/衰减。先负曲率段转动相位、再正曲率段沿衰减方向推进，在低频上有圆整作用；高频稳定方向必须同时匹配。这里没有宣称一个低频匹配自动控制所有频率。

## 4. 平面圆领的无位置边界条件（完整直接证明）

保留三个未知场 `L,M,N`，不要在 `N=0` 端用消元式。若终端 `s=S` 满足

$$a'(S)=-1,\qquad L(S,u)=M(S,u)=N(S,u)=0,$$

且前面的场确实积分成闭合标架，则自动得到半径 `a(S)` 的平面圆领。证明：终端 Weingarten 方程给

$$F_{su}=-F_u/a,\qquad F_{uu}=a F_s,\qquad n_u=0.$$

所以 `F_s+F/a=c` 与 `u` 无关，从而

$$F_{uu}+F=ac,\qquad F=ac+P\cos u+Q\sin u.$$

由 `|F_u|=a` 得 `|P|=|Q|=a,P dot Q=0`。又 `L=0` 给径向二阶法向导数为零，与平面极坐标盘的二阶 jet 完全兼容。因此可继续以 `a(s)=a(S)-(s-S)`、固定法向作平面 collar。Gauss 也自动要求终端 `a''=0`。

这说明 Gauss--Codazzi 边值法可把位置边界替换为上述局部几何条件；仍需真正求出满足这些条件的解。

## 5. 局部数值数据：没有完成圆领

脚本：`../scripts/gc_prefix_explore.py`。

### 5a. 最简余弦段

$$a(s)=a_0+.04(1-\cos10s),\quad 0\le s\le.25.$$

在固定相同几何与区间下，角网格 `64,96,128` 的终端兼容误差 `max |F_u-a e2|` 分别为

| n | 兼容误差 |
|---:|---:|
|64|1.932425e-7|
|96|1.9558124e-9|
|128|2.3943326e-11|

终端横向径向范围 `[.81857173,1.0414630]`，最大高度约 `.2459985`。沿报告的 21 个切片，主曲率绝对值最大约 `6.6706530`。它没有闭合圆领，而且 `a''(0)=4`，不能直接接椭圆柱。

### 5b. 可接椭圆柱的 ramped 段

取 `epsilon=.03,c=4,k=10`。在 `0<=s<=epsilon`，

$$a(s)=a_0+c\left[\frac{s^2}{4}+\frac{\epsilon^2}{2\pi^2}\left(\cos\frac{\pi s}{\epsilon}-1\right)\right].$$

这使 `a'(0)=a''(0)=a'''(0)=0`。在后续令 `t=s-epsilon`，

$$a(s)=a_1+\frac{c\epsilon}{2}t+\frac{c}{k^2}(1-\cos kt),\qquad
a_1=a_0+c\epsilon^2\left(\frac14-\frac1{\pi^2}\right).$$

积分到 `s=.28`，终端径向范围约 `[.84299877,1.0505700]`，最大高度 `.27433374`。96 与 128 点的终端兼容误差分别 `1.7921801e-7,9.5543226e-9`，沿 21 个切片的最大主曲率约 `6.69374`。还差完整圆整、平面端条件以及全局 reach。

复现：

```sh
python gc_prefix_explore.py --n 128 --c 4 --smax .28 --mode ramped_cosine --k 10 --ramp .03 --output gc_ramp_n128.json
```

较长的粗糙单向射击在正曲率区出现高频误差放大，不能以求解器返回 success 作为成功。比如最简余弦段延长到 `pi/10` 后，128 点的兼容误差已约 `3.9e-6`；若继续延长或加大脉冲，一些运行在 `N` 极小处爆曲率。所有这些都没有被记为闭面候选。

## 6. 对主任务的具体价值与剩余缺口

本轮已获得可用的局部等距前缀初始化、正确的 Gauss--Codazzi 系统、精确的圆领边界条件，以及曲率预算。尚没有 `Hc<.9` 的完整封帽。若继续这条线，宜用 `L,M,N,a` 的全局边值求解而不是长程椭圆 Cauchy 射击；非轴对称圆领条件未满足之前，局部圆整数据不得算作 10% 解。

## 输出身份

本地运行，不是 GitHub Actions run；再生输出不入库。下列 SHA-256 对应本次实际输出，时间参数等见各小报告；重算时浮点环境可能改变输出字节。

- gc_cos_c4k10_n128.json：`012da9d9cb3433665a03dac3653fb09b2fde709db8b560041560c3c5b71f8c51`。
- gc_c4_n96.json：`783a9c952c35bd40f359ec41794da2ff7c67d619f43c40c4f9ae0628fa28eff5`。
- gc_full_c1k6_n64.json：`00ad5348adeb63a074e2338ef17272b2b100801a0739d1cd2d36337591e838ea`。
- gc_cos_c4k10_n64.json：`0107fbf1a4848f318990d2164d70ec13725e37ee86cb9b4c993dc03d1fafbe3e`。
- gc_bvp_B1_nc24.json：`f40da0c3163aec5637e7a708f79dd7fb0b998184b115bcb0d79bccde875dea93`。
- gc_bvp_B1.json：`1f6e52236fab23d0c8b599aeb65879a5a4203e02d97d28fcfac79fca5a45ec30`。
- gc_local_prefix_n96.json：`91a26087577a217b1e781f81e473272e740e9309d951190d7f1501a097ec596b`。
- gc_local_prefix_n128.json：`036ce487f6b439f4b08044b2bb046b89a32a063c6119b05182dfe559e11cef1a`。
- gc_bvp_B09_flare04.json：`387a0ae59eeac494ca3004d5510448a8f2e589110e910c88b67cbca0c31a9676`。
- gc_ramp_n96.json：`22b9ddcc5ce139aad89771afeb1831e3d7444167dc3d843a761da71a7b1b4b91`。
- gc_local_prefix_n64.json：`d2d05e36f02ea9e14f500d873d9c83b06b1cf8f130aec16f1404a3154a453dc1`。
- gc_full_c2k8_n64.json：`c3cbf7cbd67ca2a67f148b7c6fe01dfbb2b624b975168c59b3b8e5bd03b0555e`。
- gc_ramp_n128.json：`47cd9e42136a36b9750c7e349c7378e20fdc5e370dad5a343e57293930ea04ba`。
- gc_bvp_B09_flare09.json：`8598607839253edb279680458ee93626ffff88a6ad1a83c5c6fae57654e1e56f`。
