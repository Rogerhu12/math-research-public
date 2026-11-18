# R44 圆弧 trace 空间接入真积分 oracle：源码与数学接口

状态：**接口准备，尚未在任何候选上执行 oracle、角域分盒、反函数或 metric 证书。**
本条保留 R36/R37/R41 已登记源码，新增
`scripts/resume_closed/circle_trace_core_intervals.py`。
它只替换控制函数代数；主核真积分、材料角反函数和曲线 jet 的传递公式复用原框架。
没有声称当前圆弧初猜、BVP 或闭曲面已通过。

## 1. 明确的新有限空间和输入

接口只接受 `exact_m3_circle_trace_replacement_integral`、
`circle-trace-replace-last-two-v1`、`lambda=1`、偶/C3、`eta=0`、
中心为数学的 $\pi/3$ 且锁定均值与主矩的定义。
数值 `center==math.pi/3` 只用于选择这个明确约定；不把浮点圆周常数当成数学的 $\pi$。

对 $M\ge4$，完整物理控制向量为

$$
(c_2,\ldots,c_{M-2},t,u),\qquad
b=\sum_{j=2}^{M-2}c_j B_j+tT+uU.
$$

新旧空间不可混为可逆坐标变换。特别是 M8 有全部七个控制：
五个保留的 raw 列和两个 trace 坐标；没有把最后两项当成频率 21、24 的余弦。
provenance 必须逐项提供实际 `parameters[1:]*scales` 的完整物理向量、
M、kind/path 和全部窗口参数。构造器核对这些值与实际 core 一致；
diagnostic summary 只作 family 检查，不代替物理控制定义。
本条没有读取或绑定一个尚不存在的已接受圆弧 CP。

宽度按原库的十进制往返字符串定义有理数，$q,c_j,t,u$ 按 binary64
的精确实数解释。主核的 $\beta,C$ 由实际主窗口宽度重新用 R41
真积分公式确定，不继承 R32 或 R38 的任何具体数值常数。

## 2. 低两矩投影与局部余弦

写 $L=\pi/3$、$x=\phi-L$ 在 $[-L,L)$ 的周期代表，
控制窗口为 $\chi_c(x)$，$W=1-\chi_c$。记

$$
I_k={1\over L}\int_0^{a+b_c}\chi_c(x)\cos(kx)\,dx.
$$

R44 的两列投影仍由真实矩确定：

$$
G=\begin{pmatrix}1-I_0&I_3\\I_3&(1-I_0-I_6)/2\end{pmatrix},\quad
V=\begin{pmatrix}I_0&I_1\\-I_3&-(I_2+I_4)/2\end{pmatrix},\quad D^{AB}=G^{-1}V.
$$

接口用有理区间四则运算包围上述矩与逆，必须证明
$G_{00}>0$、$\det G>0$ 才返回。
$T=S_A-S_B,U=S_B$ 对应的低投影矩阵是
$D^{TU}=(D_A-D_B,D_B)$，不是 $(D_A,D_B)$。

令 $B=u-t$，将所有保留的 raw 系数和 trace 的低两矩修正**先合并**，
得到一个有限全局三角多项式 $P$，使

$$
\boxed{b(\phi)=W(x)P(\phi)+\chi_c(x)g(x),\qquad
g(x)=t+B\cos x.}
$$

其中 $P$ 的常数项和 $\cos3\phi$ 项，分别扣去
$tD^{AB}_{iA}+BD^{AB}_{iB}$；其余保留的高次项由原 raw 定义给出。
这一步保留 $T=S_A-S_B$ 的抵消。

这里的 $\cos x$ 只出现在 $\chi_c g$ 内。
$a+b_c<L$ 保证该乘积在周期代表接缝附近恒零，所以没有将局部
$\cos x$ 当作一个独立的全局周期谐波。
其 C4 正则性和偶/C3 对称由 R44 的同一窗口构造保留。

## 3. 控制 jet、原函数和组合曲率预算

若 $P(\phi)=\sum_k D_k\cos(3k\phi)$，则在局部变量中
$\cos(3k\phi)=(-1)^k\cos(3kx)$。
接口直接以乘积法则计算 $b$ 的零至五阶分片 jet。
第五阶只作为分片界使用，不宣称跨窗口接点连续。

相应的奇原函数为

$$
\begin{aligned}
J_b(x)={}&\sum_k(-1)^kD_k
 \left\{\int_0^x\cos(3ks)\,ds-\int_0^x\chi_c(s)\cos(3ks)\,ds\right\}\\
&+t\int_0^x\chi_c(s)\,ds+B\int_0^x\chi_c(s)\cos s\,ds.
\end{aligned}
$$

全部 cutoff 原函数调用 R41 的自选 Taylor 阶数接口；其完整余项先以有理数
验证，再选择阶数。控制矩所需最大频率是 $3(M+1)$，也覆盖新的局部频率 1 至 6。
原库中 32 点或 64 点 Gauss 求值不是这个区间原函数的定义或界。
精确低均值给 $J_b(L)=0$，偶对称给反射轴上的 $b'=0$，
故原材料角原点仍保持 $u(0)=0$ 和 $u(L)=L$。

为避免先把两列分开取绝对值，曲率扰动使用恒等式

$$
b+b''=W(P+P'')+2W'P'+W''P
          +t\chi_c+2\chi_c'g'+\chi_c''g.
$$

特别是 $g+g''=t$ 已在估计之前消去局部余弦。
对该式再求零至三阶导数，按 Leibniz 法则用同一真 cutoff 导数界和
有限三角多项式系数包围。所有输入系数及范数求和均为有理区间/有理数运算，
没有浮点求和未经外包而当界的问题。

在 cutoff 支持上，写 $e=a+b_c$，可取

$$
|g|\le\min\{|t|+|B|,\ |u|+|B|\min(2,e^2/2)\},\qquad
|g^{(2r+1)}|\le |B|\min(1,e),\quad |g^{(2r)}|\le|B|\ (r\ge1).
$$

这些较紧界只用于至少带一个 $\chi_c$ 或其导数的项；在其支持外相应乘积为零。
$WP$ 项使用全角三角多项式范数，不将局部 $g$ 界误用于整个周期。

输出包括解析的全角 $\rho$ 下/上界和 $\rho_\phi,\rho_{\phi\phi}$、
分片 $\rho_{\phi\phi\phi}$ 上界。解析下界可能非正；这不等于核心实际非正，
也不会被自动改成源数值 guard 的正值。
后续如需较紧曲率包围，可明确调用另备的中点加全 panel Lipschitz 余项接口；
本条未执行该调用。

## 4. 复用 R36/R37 的条件与来源误差

R36 的 normal-jet 公式只通过 $b,b',\ldots,b^{(4)},J_b$ 读取控制，
因此上述替换足以进入相同真 $\Gamma$、弧长和法向量公式。
R37 的材料导数上界与五阶分片余项继续需要一个**已经证明为正**的全角
$\rho$ 下界。新类不绕过这个前提。
接口也不把某些有限点值自动扩大成全角界。

新类另包围实际 binary64 raw/trace 投影系数与真投影的差，
但只将其标为**投影系数误差**。
源 cutoff、三角函数、Gauss 原函数、反函数和完整源 jet 的数值误差仍须另付；
不能仅凭这个系数误差宣称源图和真 core 已在某个统一阈值内。
旧 R36/R37/R39 的某个具体候选数值界不自动移植到这个新核。

物理度量与共同材料域继续用 R41 的 `fixed_atlas_identity` 原样绑定。
core 变动本身不证明同 g；$\delta$、物理尾输入或 $L_{\rm binary}$ 若改变，
就必须按实际新候选重新绑定。旧原有限图误差、闭帽、公共接缝、直径和 reach
仍各自需要验收。

## 5. 可读出的局部圆弧恒等式

在公共保护弧上，接口返回

$$
R=1+8q+t,\qquad c=qC-(u-t),\qquad
O=-c\,e_r(\pi/3),\qquad u(\pi/3)=\pi/3.
$$

它们只是 R44 的实际圆心符号与半径作用在本接口里的直接表达。
半径正性、轨迹开邻域、非零标记、完整曲面的直径和最终握持比例都没有据此自动成立。

本条伴随记录 `circle_trace_core_interval_interface.json` 只固定源码/依赖身份和
语法读取范围；没有生成 oracle 数值输出，没有重算已登记的旧候选或旧结论。


复现本条元数据读取（输出必须使用新的文件名，以免覆盖已登记记录）：

```bash
python topics/visible-flex-held-10pct/scripts/resume_closed/record_circle_trace_interval_interface.py --out /tmp/circle-trace-interface-metadata.json
```

本次实际元数据命令的工具记录为 `16a1f2`，真实退出码为 0；
仓库内输出 SHA-256 为
`0f146f72238d2ad1e6c3551779ae334414e1db96c24662e6fa9488960f968e26`。
此退出只证明该次语法读取与来源记录完成，不是 oracle 数值执行记录。
