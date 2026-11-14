# R194 — 实际主曲率双侧上界的有理区间半正定消费者

## 1. 范围与输入身份

本结果给出一个可直接消费 R193 实际两 jet 区间的充分证书层。它不构造这些区间，也不把 R191 的采样曲率、旧 formal II 或数值 guide 当作连续曲率界。

设 $X$ 是一个 $C^2$ 曲面参数化，所有输入必须对应同一准确参数定义、同一物理坐标 $(s,u)$ 和同一闭物理盒。调用者须给出各分量的有效区间，及其定义、盒和证据身份。本文的判据在每一点与实际曲率条件等价；用独立区间代入后的通过条件仅是充分的，未决不表示曲面不存在或该上界为假。

本结果允许参数网格的结点、分段的 $C^2$ 接口和闭角区间。若用分段盒覆盖接口，须确实覆盖对应的连续两 jet 或两个相容的单侧闭包。这里不要求径向三阶导数。

## 2. Gram 形式的精确判据

记实际第一、第二基本形式的矩阵为

$$
H=\begin{pmatrix}E&F\\F&G\end{pmatrix}>0,\qquad
Q=\begin{pmatrix}L&M\\M&N\end{pmatrix}.
$$

它们可以取原坐标，也可以取同一个任意非奇异切基。实际主曲率是对称矩阵 $H^{-1/2}QH^{-1/2}$ 的两个特征值。对 $C\ge0$，

$$
\max_i|\kappa_i|\le C
\quad\Longleftrightarrow\quad
CH+Q\succeq0,\quad CH-Q\succeq0. \tag{1}
$$

证明：将两侧分别以 $H^{-1/2}$ 作合同变换，得到 $CI\pm H^{-1/2}QH^{-1/2}$。它们同时半正定，正好等价于每个特征值位于 $[-C,C]$。这一步也证明判据与切基的选择无关。

实对称二阶矩阵半正定，当且仅当两个对角元和行列式均非负。因此令

$$
A=C^2\det H+\det Q,\qquad
B=EN+GL-2FM,
$$

式 (1) 等价于六个标量条件

$$
CE\pm L\ge0,\qquad CG\pm N\ge0,\qquad A\pm CB\ge0. \tag{2}
$$

其中

$$
\det(CH\pm Q)=C^2(EG-F^2)+(LN-M^2)
 \pm C(EN+GL-2FM).
$$

全部六个量严格为正时，两矩阵正定，得到 $\max_i|\kappa_i|<C$。实际实现还先证明 $E>0$ 和 $\det H>0$。若任一个必要正性没有被输入区间付清，消费者返回未决。

这不是用第二基本形式的分量大小代替主曲率；实际 Gram 矩阵完整保留在式 (1)–(2) 中。

## 3. 原 Cartesian 两 jet 的无平方根式

取

$$
U=X_s,\quad V=X_u,\quad W=U\times V,\quad D=W\cdot W,
$$

并设

$$
E=U\cdot U,\quad F=U\cdot V,\quad G=V\cdot V,
\qquad
B_{ij}=W\cdot X_{ij}.
$$

若 $D>0$，则 $EG-F^2=D$，且 $Q=B/\sqrt D$。式 (1) 等价于

$$
C\sqrt D\,H+B\succeq0,\qquad
C\sqrt D\,H-B\succeq0. \tag{3}
$$

写

$$
J=B_{11}B_{22}-B_{12}^2,\qquad
M_B=E B_{22}+G B_{11}-2F B_{12},\qquad
A_B=C^2D^2+J.
$$

利用准确恒等式 $\det H=D$，两行列式为

$$
\det(C\sqrt D\,H\pm B)=A_B\pm C\sqrt D\,M_B.
$$

因 $C,E,G,\sqrt D$ 非负且 $E,G,\sqrt D$ 实际严格为正，式 (3) 等价于以下四个多项式条件：

$$
\begin{aligned}
P_{11}&=C^2DE^2-B_{11}^2\ge0,\\
P_{22}&=C^2DG^2-B_{22}^2\ge0,\\
A_B&\ge0,\\
P_{\det}&=A_B^2-C^2D M_B^2\ge0.
\end{aligned} \tag{4}
$$

前两式分别等价于两个对应对角元的正负条件；后两式等价于 $A_B\ge C\sqrt D\,|M_B|$，即两行列式均非负。保留 $A_B\ge0$ 是必要的，不能只检查平方后的最后一式。

所以，只需在完整盒上证明 $D>0$ 并给出式 (4) 四个量的非负区间下界，就获得实际主曲率双侧界。全部四个下界严格为正则得到严格界。此版本既不求特征值，也不求平方根。各量之间的相关性通过准确恒等式先消去；其余区间相关性丢失只会造成未决。

## 4. R187/R190 的单位切向量归一版本

对准确位置定义

$$
X_u=aT,\qquad |T|=1,\qquad a>0,\qquad V=X_s,
$$

在点态切基 $(X_s,X_u/a)$ 下，

$$
H=\begin{pmatrix}|V|^2&V\cdot T\\V\cdot T&1\end{pmatrix},
\quad
W=V\times T,\quad D=|W|^2=|V|^2-(V\cdot T)^2.
$$

因为 $N=W/\sqrt D$ 且 $N\cdot T=0$，

$$
\begin{aligned}
Q_{ss}&=N\cdot X_{ss},\\
Q_{su}&=N\cdot \frac{X_{su}}a
       =N\cdot\left(\frac{a_s}aT+T_s\right)
       =N\cdot T_s,\\
Q_{uu}&=N\cdot\frac{X_{uu}}{a^2}
       =N\cdot\frac{T_u}a.
\end{aligned} \tag{5}
$$

因此式 (4) 可直接使用

$$
B_{11}=W\cdot X_{ss},\qquad B_{12}=W\cdot T_s,\qquad
B_{22}=\frac{W\cdot T_u}{a},\qquad G=1. \tag{6}
$$

这里准确消去了混合项中的 $a_sT/a$，并且法向用 $V\times T$ 归一，避免再引入一个半径因子。对 $D$ 的两种准确表达分别作区间并取交，可进一步收紧；交为空表示调用者的声称区间或身份不一致，程序拒绝输入。

这些公式针对完整的准确单位切向量。有限 Fourier 截断或采样的近似 $T$ 不能仅因接近单位而使用 $G=1$；那种输入须用 Cartesian 入口，或先由 R193 完整误差层付清准确 $T$ 的关系。

## 5. 与 R193 的明确衔接

R193 输出实际准确相对度量区间 $r_E,r_F$，且由完整位置定义有 $r_G=0$。因此本消费者取

$$
H_{11}=1+r_E,\qquad H_{12}=r_F,\qquad H_{22}=1. \tag{7}
$$

另需调用者提供同一个参考 $Q_0$ 的已证分量区间。这里的参考准确含义必须是

$$
Q_0=N_0\cdot
\left[X_{ss,0},\ T_{s,0},\ T_{u,0}/a_0\right],
$$

并使用 R193 已纳入的参考法向误差约定。若 R193 的
second_form_error.L、M、N 给出非负准确误差
$\epsilon_L,\epsilon_M,\epsilon_N$，则实际 $Q$ 的合法区间是

$$
Q_{11}\in [Q_{0,11}]+[-\epsilon_L,\epsilon_L],\quad
Q_{12}\in [Q_{0,12}]+[-\epsilon_M,\epsilon_M],\quad
Q_{22}\in [Q_{0,22}]+[-\epsilon_N,\epsilon_N]. \tag{8}
$$

将式 (7)–(8) 送入式 (2) 即可。消费者核对声明的 R193 bindings 与参考输入 bindings 完整一致，并要求相同 scope、明确物理盒、参考定义及证据。该结构核对不能替代调用者对区间本身的证明。

此入口不需要从采样特征值猜测 $Q_0$ 区间，也不调用 R193 的旧参考曲率上界作为分量区间。R193 中的所有 primitive、中央曲线、准确 grid 和 scalar profile 误差仍由其各自的证据承担，本结果不重复构造。

## 6. 有理区间实现和可消费接口

源文件：[fd2d-position-curvature-certificate-R194.cjs](../scripts/fd2d-position-curvature-certificate-R194.cjs)。

工厂 createR194CurvatureCertificate() 返回：

- certifyCartesianJetBox(packet, cap)：packet.jets 为 Xs、Xu、Xss、Xsu、Xuu。
- certifyUnitTangentJetBox(packet, cap)：packet.jets 为 V、T、Ts、Tu、Xss、a；须明确式 (5) 的准确单位切向量及位置身份。
- certifyFormBox(packet, cap)：packet.H 和 packet.Q 为对称三元组 [11,12,22]；可给另一已证 detH 区间取交。
- fromR193Budget(budget, reference, cap)：按式 (7)–(8) 构造上述输入。

每个区间可用 lower/upper（或 lo/hi），端点使用整数字符串、分数字符串或 [numerator,denominator]。若输入 binary64 数，程序将该实际二进制数准确转换成有理数；这不把它变成未付的准确几何端点。所有四则运算、乘法取端点极值、跨零平方、正负比较均用 BigInt 有理数完成。区间除法拒绝含零分母。结果完整保留准确有理下上界，不依赖显示小数。

返回 passed 仅表示：在所声明完整区间前提下，该盒通过。strict_cap_proved 另表示上述严格余量全部通过。未决量逐项列出，不视作无解。该模块不宣称已覆盖主候选或闭曲面。

若后续对一个准确物理域给出有限闭盒覆盖，每个盒都通过相同 cap，则由逐点覆盖得到整域上界；phase 族的刚体变换若按其准确公式成立，可再按该公式传递曲率。完整闭面的 reach、跨片法球、held 和固定帽接合仍须分别支付，不能从局部曲率界推出。

## 7. 已执行的小消费者与明确范围

检查源：[fd2d-check-position-curvature-certificate-R194.cjs](../scripts/fd2d-check-position-curvature-certificate-R194.cjs)。

本组纯 JavaScript/V8 实际完成，耗时 7 ms；没有 OS 子进程或 shell exit code，也没有 BVP、whole normal 或实际坏场 body。原始有理报告另存 notes。

1. 连续解析二次图
   $X(s,u)=(s,u,s^2+su/2-u^2/2)$，
   $|s|,|u|\le1/100$，由准确多项式导数给盒，证明 $|\kappa_i|<21/10$。式 (4) 的最低余量均严格为正。
2. 同图原点 cap $2$ 未通过。准确向量 $(10,1)$ 的二次型值为 $209$，Gram 能量为 $101$，所以实际某个主曲率至少 $209/101>2$。这个反例只验证错误上界不会被接受。
3. 同一原点的 $3$–$4$–$5$ 正交切基变换和两个方向分别缩放 $3,2$ 后，式 (2) 仍证明 cap $21/10$。
4. 连续圆柱 $X(s,u)=(s,\sin u,-\cos u)$，$|u|\le1/100$：用
   $|\sin u|\le1/100$、
   $1-u^2/2\le\cos u\le1$ 的严格盒及完整单位切向量，证明 cap $1001/1000$。同一较粗区间对准确可达的 cap $1$ 返回未决，说明区间依赖可能使一个真的界未被当前盒证明。
5. R193 的非零条件算术 fixture，加上明确假设的同盒参考 $Q_0=(6,0,-5)$，经真实 adapter 证明 cap $15/2$。这只是错误合成和输入路由核，不是 B32 的实际区间证书。

这些 fixture 不给当前 R187/R190 接受态任何全域几何认证。当前候选仍需实际的中央、primitive、准确 scalar 和 grid 证据组成真实盒后，再调用本消费者。
