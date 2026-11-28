# 正确 Phi 第二个 NV 最高头：两个完整 odd 原值、八条新列与两个固定九原 cofactor

**状态：新的未执行输入。** 已完成的第二头二十列/三个 cofactor 不重跑。这里第一次加入同一原点的完整 singleton $N/P$ 误差的两个奇部；只生成这两个新式的八条基倍列，并形成事先固定、同时含两个新式的两个四阶 cofactor。全程保留其他原条件与全部新头零纤维。

源码：同目录 **2026-11-28-unit211-Phi-zero-corrected-second-NV-head-complete-odd-NP-eight-original-columns-8542.py**。

源码 SHA-256：
39a56877bf4a1ccb73432b9d70dc73c840c22c3415b9bd6cbc3de6c3e3834252。

资源预定：**绝对 120 秒、1 GiB；外层 135 秒**。唯一直接依赖见 §7；不在本说明中预报任何执行结果。

## 1. 当前原图与两个首一关系

范围仅为当前已经纠正的 $\Phi=0$ 原图与第二个完整 $NV$ 的 $t$ 首项因子
$$
B_2=\ell(3-2\lambda)+2T+2m\sigma=0.
\tag{1}
$$
采用既有原符号
$$
s=u-1,\quad \delta=1-Q,\quad
L=Q-2s(u-2),\quad \ell=L/Q,\quad m=u-\ell,
$$
$$
T_0=-K_w,\quad K_w=Q+4s,\quad
P_{02}=2sL,\quad J-Q=-4s^2,\quad
M=Q^{-1}M_n=4bc\delta.
$$
实际代码只使用由
$$
P_{\mathrm{old}}=Q\delta sK_wLM_n
\tag{2}
$$
生成的原权单位支持。这里不新增 $m,u,2\ell-1$、任一新 $\lambda$ 头、$D$、$\sigma$ 或 $t$ 的逆。

在 (1) 上
$$
a=\lambda-\frac32,\quad T=\ell a-m\sigma,\quad
E=\frac{P_{02}(T+\ell)}{T_0},
$$
$$
f=\frac{P_{02}\lambda-QE+sT_0}{J-Q},\qquad
V=f+bct-E,\qquad A_1=2E.
\tag{3}
$$
原 Gram 坐标沿既有同点公式恢复，满足正确 dual 乘法。特别
$$
h=\lambda-\frac12-\rho\sigma,\qquad
k=\lambda-\frac12+\rho\sigma,\qquad \rho^2=\delta.
\tag{4}
$$
不令物理 $t$ 等于零。

已经证明并实际返回的两条首一关系为
$$
q_\sigma=\frac{E_2}{\ell\delta}
=\sigma^2-\frac{2ma}{\ell\delta}\sigma
-\frac{A_\lambda-\ell a^2}{\ell\delta},
\qquad A_\lambda=2\lambda^2-2\lambda+1,
\tag{5}
$$
以及
$$
q_t=\gamma_R R+\gamma_O E_{Bo},
\quad
\gamma_R=-\frac{B_q}{\ell bc\,sQ},
\quad \gamma_O=-\frac{8\delta}{\ell},
\tag{6}
$$
其中
$$
B_q=Q^2+(2u^2-3)Q+2s(2u-1)(u-2).
$$
正确原均值 $R$ 是
$$
R=4(f-u)(V-f)+bc\,t^2+
t\left(4bcu-\ell V+
\frac{m(T_0+4uf-2V)}{2\delta}\right).
\tag{7}
$$
其 $t^2$ 系数与 $E_{Bo}$ 的 $t^2$ 系数已经给出
$\gamma_R[t^2]R+\gamma_O[t^2]E_{Bo}=1$。

定义唯一普通短除
$$
q_t=\widetilde q_t+w_\sigma q_\sigma,
\qquad \deg_\sigma\widetilde q_t<2.
\tag{8}
$$
$\widetilde q_t$ 对 $t$ 首一二次，故
$$
\mathcal B=
\mathcal A[\lambda,\sigma,t]/(q_\sigma,\widetilde q_t)
$$
在原权系数环 $\mathcal A[\lambda]$ 上为真正自由四生成环境，基固定为
$$
e=(1,\sigma,t,\sigma t),\qquad d=(0,1,1,2).
\tag{9}
$$
所有重根和幂零结构保留。再商原值理想后的模不被宣称自由。

来源：

- [全权首一 $t^2$ 与四元环境](../results/R150-appendix-unit211-Phi-zero-corrected-whole-monic-t-quadratic-exact-ten-columns-and-four-generator-NV-head.md)；
- [第二头二十原列及三个原 cofactor](../results/R150-appendix-unit211-Phi-zero-corrected-second-NV-t-head-twenty-original-columns-and-three-cofactors.md)，唯一实际 run 46170068898、job 141056253058；
- [两个一般 odd 原范数的原误差定义](../results/R150-appendix-unit211-general-original-odd-NP-two-direct-sextic-norms.md)。

## 2. 新的两个完整原值

令 $v_B=(p,r,0,t)$、$v_C=(q,s_G,t,0)$ 为同一原 Gram 的两个 singleton 行，$\tau$ 和乘法仍是原 dual 代数；第一块第二坐标乘法为
$$
(vw)_1=v_0w_1+v_1w_0.
$$
设
$$
P_2(v)=\tau\!\left((v-\tau(v)\mathbf1)^3\right)
$$
并使用完整原定义的 $N_4(v)$。新输入是
$$
E_N=\bigl(N_4(v_B)-2\lambda P_{02}h^2\bigr)_{\rm odd},
\qquad
E_P=\bigl(P_2(v_B)-P_{02}h^3\bigr)_{\rm odd}.
\tag{10}
$$
这里 odd 表示 $\rho$ 的系数，不是省略中心项或用一个加权值替代。代码独立构造两个共轭 singleton 的完整误差，返回共轭身份与
$$
\mathrm{Err}_{N,B}-\mathrm{Err}_{N,C}=2\rho E_N,\qquad
\mathrm{Err}_{P,B}-\mathrm{Err}_{P,C}=2\rho E_P.
\tag{11}
$$
这只记录原代数相等，不把单个 odd 值充分化为两个完整 singleton 值。

(3) 中全部几何量仿射，故 $E_N,E_P$ 的总 $(\lambda,\sigma,t)$ 次数至多三。代码在新目标中核此上界。所有原 even 值、原加权 $NS/PS$ 与其他原条件继续保留；没有以 (10) 代替完整物理系统。

原式次序固定为
$$
(F_0,\ldots,F_8)=
(E_2,R,E_{Be},E_{Bo},N_1,E_3,NV,E_N,E_P).
\tag{12}
$$
$NV=N_4(1,w,h,k)$ 是完整、未乘 $\ell^2$ 的值；$E_3$ 是第三矩误差。前七式的定义来源不变。

## 3. 仅新增八列，精确的合并呈示

对任意新 $G$，先对 $\widetilde q_t$ 作普通首一 $t$ 除法，再对 $q_\sigma$ 作普通首一 $\sigma$ 除法：
$$
G=r+Q_t\widetilde q_t+Q_\sigma q_\sigma.
$$
使用 (5)、(6)、(8)，得到完整普通多项式身份
$$
G=r+
\frac{Q_\sigma-Q_tw_\sigma}{\ell\delta}E_2+
Q_t\gamma_RR+Q_t\gamma_OE_{Bo}.
\tag{13}
$$
余式 $r$ 唯一写在 (9) 中。这是原式来源，不需要把原值商假设为自由或把未经验证的矩阵相乘当作结合代数。

本次只对
$$
E_N,\ \sigma E_N,\ tE_N,\ \sigma tE_N,\qquad
E_P,\ \sigma E_P,\ tE_P,\ \sigma tE_P
\tag{14}
$$
生成八条新列、返回八次 (13) 及全部三十二个四元坐标。对新种子 $F_i$ 的第 $j$ 个基倍，坐标第 $r$ 行满足
$$
\deg_\lambda c_{rj}\le 3+d_j-d_r.
\tag{15}
$$

此前 $J_7=(F_0,\ldots,F_6)$ 的二十列已经实际支付。本次合并的
$J_9=(F_0,\ldots,F_8)$ 因而具有精确 $4\times28$ 呈示：旧二十列加 (14) 的八列。原因是四元环境在 $\mathcal A[\lambda]$ 上以 (9) 为基，每个新理想生成元的任意倍数都由其四个基倍生成。这个推论不要求重新生成旧二十列。

旧列编号保持：$R$ 块从 $0$ 开始，$E_{Be}$ 块从 $4$ 开始，$N_1$ 块从 $8$ 开始；新 $E_N$ 块编号 $20,\ldots,23$，新 $E_P$ 块编号 $24,\ldots,27$。代码仅为下一固定矩阵再生旧的三个基列定义 $0,4,8$；不进入旧二十列循环、不重返旧三个 cofactor，也不计算它们的共同 gcd。

## 4. 两个事前固定的新原 cofactor

唯一两个固定组是
$$
\mathcal S_N=[0,4,20,24]=[R,E_{Be},E_N,E_P],
$$
$$
\mathcal S_J=[0,8,20,24]=[R,N_1,E_N,E_P].
\tag{16}
$$
二者都含两个新 odd 值，不依实际结果改列。对应 $4\times4$ 矩阵记作 $B$。采用固定的 adjugate 第一列
$$
\omega_j=(-1)^j\det B_{\widehat0,\widehat j},
\qquad
B\omega=(\det B)e_0.
\tag{17}
$$
四个坐标全部乘回。没有倒 $\det B$、其中任何主元或任何新的 $\lambda$ 首项。

两组列的总几何次数分别为 $(2,2,3,3)$，基权之和为四，故
$$
\deg_\lambda\det B\le2+2+3+3-(0+1+1+2)=6.
\tag{18}
$$
这是预定上界，不是实际六次或非零的预报。

将 (17) 的四列沿 (13) 反传，得到
$$
\det B=\sum_{i=0}^{8}\beta_iF_i
\tag{19}
$$
的完整九原身份。$E_3$、$NV$ 的乘子可以为零；它们仍属于实际同点原系统，且其原条件未被删掉。

## 5. 只约消全部真实原乘子的共同因子

写 $F_i=n_i/d_i$，其中各 $d_i$ 只有 (2) 的原权支持。代码先使用真实乘子 $\beta_i/d_i$，再把全部九项及右侧统一清分母：
$$
\sum_{i=0}^{8}\Omega_i n_i=C.
\tag{20}
$$
只有在 (20) 全式返回之后，才计算全部九个实际 $\Omega_i$ 的共同因子 $g$，逐项精确除去并把右侧也精确除 $g$，再次返回完整 (20)。这是多项式身份的共同约消，覆盖 $g=0$ 的整个纤维，不把 $g$ 当物理单位。

此后只允许剥除 (2) 的已付权因子并作非零有理常数规范；相同尺度运输到九个原乘子，最后普通原式再次返回。所有最终实际分母逐一只按旧支持检查。

没有新的 $\lambda$ 首项单位测试、QQ 因式分解、三标量泛域 gcd、数值素数、DVR 筛选或原点选择。新必要式若非零，其所有新头零面保留；只有真正返回原常数单位才可排除当前整个第二头。新式零或资源截止时，准确保存最后完整返回阶段，不外推排空。

## 6. 当前结果边界

此前三式实际 $\lambda$ 次数为 $5,6,6$，但未返回单位；第二头仍开放。本次不把这一已成目标重包装为 gcd 门。

即使本次两式返回，其范围也是 (1) 中的原必要条件及精确 $J_9$ 呈示，不是全 $\Phi$ 排除，不把有限自由的四元环境等同于原值商自由，也不从次数、term 数、规范 hash 或单个必要式非零推出原纤维空。

## 7. 唯一依赖与实际执行边界

直接依赖仅：

**2026-11-28-unit211-Phi-zero-corrected-second-NV-t-head-original-four-generator-columns-8542.py**

- 完整 blob：d20becf217080f2f22bbe5b696822d3cddca9ec4；
- 完整 SHA-256：c7141ce12424d916ee415c0ac0121ea938ff206d20b5a8c12193bb3a1cdcdaa1；
- 唯一必要定义前缀：前 **10519** 字节，终止于注释 “# EXACT source order and all twenty columns are fixed before execution.” 之前；
- 前缀 SHA-256：67c407b2bd4a611a90a1094403546860459dfbb3bad6676a990dca6773343255。

完整文件和前缀各自先核 SHA。AST 仅保留参数赋值、类、函数和 imports；去掉旧顶层断言、输出、计数、原坐标分母检查循环及顶层时钟/资源调用。内部精确算术和首一短除的返回仍保留。必要前缀不读取其他文件。

外层最初设定唯一绝对 120 秒 alarm 和 1 GiB 硬限，必要前缀不能重设或关闭。旧二十列和旧三个 cofactor 位于前缀之后，根本不进入新执行；三个旧基列仅作为 (16) 所需参数以唯一首一短除定义再生。新源只输出 profile、次数、hash、实际阶段和全式返回计数，不输出或持久保存可再生系数载荷。

若发生资源边界，冻结本次未完成目标，不增加预算、改变固定列或续跑同一证明段。
