# R725　闭纬圈的实物坐标、全族共用径向度量与两端刚帽

**已证明。** 本条给真正闭合纬圈的完整坐标、全部材料二 jet，以及在所有时间共用同一个 $g=E(r)dr^2+r^2d\phi^2$ 时的精确可行区和最佳误差。目标积分及普通离散读数均不冒充精确等距或全壳几何。

## 1　真实闭圈坐标与固定材料导数

设 $a\le r\le b$，$\Gamma(r,\psi)$ 为真正 $2\pi$ 周期的正则空间曲线族，$v=|\Gamma_\psi|>0$，下文所用混合导数存在且连续。按 $d\psi/(2\pi)$ 取均值，令
$$
L=\langle v\rangle,\quad J=v/L,\quad
\Phi(r,\psi)=\int_0^\psi J(r,s)\,ds,\quad
M=\langle\Gamma J\rangle,\quad U=(\Gamma-M)/L.
$$
$\Phi(\psi+2\pi)=\Phi(\psi)+2\pi$，所以有升向逆 $\Psi$。定义物理材料图
$$
F(r,\phi)=C(r)+rU(r,\Psi(r,\phi)).
$$
于是
$$
F_\phi/r=T=\Gamma_\psi/v,\quad |T|=1,\quad
\langle T\rangle_\phi=0,\quad
\int_0^{2\pi}|F_\phi|\,d\phi=2\pi r.
$$
每圈严格闭合，$C$ 是真实弧长重心。这也是所有正则定长纬圈的坐标：任一此种实际 $F$，取 $\Gamma=(F-C)/r$、$\psi=\phi$，就有 $L=J=1$，原图准确复原。

若 $\Gamma(-\psi)=\operatorname{diag}(1,-1,1)\Gamma(\psi)$，则 $J$ 偶、$\Phi$ 奇，$\psi=0,\pi$ 的材料标识固定。要使整个 $F$ 保持这一反射，$C$ 也须在其不动平面。

置
$$
\gamma=\Phi_r/J,\qquad D=\partial_r-\gamma\partial_\psi,\qquad
\partial_\phi=J^{-1}\partial_\psi.
$$
两算子由 $\partial_\psi\Phi_r=J_r$ 交换。固定材料 $\phi$ 的完整二阶数据为
$$
F_r=C'+U+rDU,\qquad F_{rr}=C''+2DU+rD^2U,
$$
$$
F_{r\phi}/r=T/r+DT,\qquad F_{\phi\phi}/r^2=T_\psi/(rJ),
$$
其中
$$
D^2U=U_{rr}-2\gamma U_{r\psi}+\gamma^2U_{\psi\psi}
       +(\gamma\gamma_\psi-\gamma_r)U_\psi.
$$
实际实现须支付 $L,\Phi$ 及其径一、二导的角积分、同材料角的反求，以及真实 Gram、法向和形算子。连续积分定义与有限实现分别登记。

## 2　真平圈端锚和完备法图自由度

内外端的充分锚是 $\Gamma=Qe_r(\psi)$、$\Gamma_r=\Gamma_{rr}=0$，所需混合角导同一；$C'=C''=0$。内端 $Q$ 为指定倾转，外端 $Q=I,C=0$。于是 $L=J=1$，它们以及 $\Phi$ 的两径导均零；实际六 jet 准确为
$$
C+rQe_r,\quad Qe_r,\quad Qe_\phi,\quad 0,\quad
Qe_\phi/r,\quad -Qe_r/r.
$$
曲线扰动取端部 $O(h^3)$ 可保两阶；重心的端两导固定为零，同时允许内重心真平移。

参考切向不竖直时，可取
$$
n_1=\frac{e_z-(e_z\cdot T)T}{|e_z-(e_z\cdot T)T|},\qquad n_2=T\times n_1.
$$
参考闭曲线有正管宽时，任一充分 $C^1$ 接近的嵌入圈，按管内垂足重标后可写成这两个法方向的法图。上述反射下 $T(-\psi)=-RT(\psi)$，因 $\det R=-1$，两个 $n_i$ 均按 $R$ 变换，可配偶标量。有限空间中的平移、缩放、重标或其他规范方向须实际登记，不能因此删除未证冗余的小奇异方向。

## 3　所有时间共用一个 $E$ 的精确区间

令时间集紧，所有 $F_t$ 定义在同一材料 $(r,\phi)$，且 $|F_{t,\phi}|=r$。固定 $r$，索引 $i=(t,\phi)$ 遍历全部时间、材料角。置
$$
A_i=|F_{t,r}|^2,\qquad B_i=F_{t,r}\cdot T_t,\qquad b_i=B_i^2.
$$
浸入给 $A_i>b_i$。相对 $g=Edr^2+r^2d\phi^2$ 的 Gram 误差矩阵为
$$
\begin{pmatrix}A_i/E-1&B_i/\sqrt E\\ B_i/\sqrt E&0\end{pmatrix}.
$$
对 $0<\eta<1$，两个 $\pm\eta I$ 的 Schur 补表明：全族算子误差至多 $\eta$，当且仅当唯一共用标量满足
$$
E_{\rm lo}(r,\eta):=\max_i\frac{A_i+b_i/\eta}{1+\eta}
\ \le E(r)\le\
E_{\rm hi}(r,\eta):=\min_j\frac{A_j-b_j/\eta}{1-\eta}. \tag{1}
$$
$i,j$ 可以来自不同时间，不能各时间独选 $E$。

任一下界小于任一上界，等价于
$$
(A_i+A_j)\eta^2+(A_j-A_i+b_i-b_j)\eta-(b_i+b_j)\ge0.
$$
令 $d_{ij}=A_j-A_i+b_i-b_j$，该二次式的最大非负根是
$$
\eta_{ij}=
\frac{\sqrt{d_{ij}^2+4(A_i+A_j)(b_i+b_j)}-d_{ij}}
 {2(A_i+A_j)}.
$$
在 $b_i=b_j=0$ 时准确为 $\max(0,(A_i-A_j)/(A_i+A_j))$。故
$$
\eta_{\rm best}(r)=\max_{i,j}\eta_{ij}. \tag{2}
$$
在 $\eta=1$ 时，每对二次式等于 $2(A_j-b_j)>0$，紧性给 $\eta_{\rm best}<1$。取 $i=j$ 即得任何 $E$ 都无法去除的单点下界 $|B_i|/\sqrt{A_i}$。

若 $\eta_{\rm best}>0$，某对上下界准确相等，最佳 $E$ 因而唯一。若 $\eta_{\rm best}=0$，所有 $B_i=0$、所有 $A_i$ 相等，最佳 $E$ 就是该公共值。

## 4　共同光滑度量与目标积分的选择

若全部输入在紧 $(r,t,\phi)$ 域连续，(1) 两端及 (2) 连续。令 $\eta_0=\max_r\eta_{\rm best}(r)$。任意 $\eta_0<\eta<1$ 下，$E_{\rm lo}<E_{\rm hi}$ 在全径有统一正余量。真刚帽端有 $A=1,B=0$，所以 $1$ 严格落在端区间内，可在足够小端领指定 $E\equiv1$。

内域的连续区间中点可一致平滑近似，再与平端拼接，得到一条完整光滑正 $E$ 保持严格资格。若
$$
\int_a^b\sqrt{E_{\rm lo}}\,dr<S_{\rm goal}
 <\int_a^b\sqrt{E_{\rm hi}}\,dr,
$$
先在尽可能短端领以外分别从内侧逼近上下界，构造两条平滑正函数，端领接一，积分夹住 $S_{\rm goal}$。二者凸插值始终在同一区间，积分连续，因而可准确指定共同的 $\int\sqrt E\,dr$。这是设计自由度；未等距时不能把它叫作实物母线长度，也不自动支付 R665 的端位和切向门。离散角、径或时间输入只授相应离散结论。

R680 proper 材料旋转特例的各时 Gram 只是材料角平移，故一个基相位整圆已覆盖全部时间；一般族没有这个简化。

## 5　原 R680 圆基不能仅靠选 $E$ 过门

原真圆基有 $B=0$、
$$
A=1+p^2(1.01+\cos\phi)^2.
$$
所以唯一最佳
$$
E=1+2.0201p^2,\qquad
\eta_{\rm best}=\frac{2.02p^2}{1+2.0201p^2}.
$$
原端倾转要求 $\int_a^b|p|\,dr/r=\arcsin(.27)>.27$，而
$\log(b/a)=\log(44/15)<1.1$，故某半径 $|p|>27/110$，在该处 $\eta_{\rm best}>.10$。这只排除原未改形状靠选择 $E$ 达到 $10^{-6}$；原厚壳和位移见证不被取消。

## 6　已付实物曲线进入新坐标的准确代价

对 R703/R718 任一真正旧闭原函数 $A$，保存原中心 $C_0$、材料映射 $\Phi_0$ 和具体参考角/径实现。若连续定义为
$$
A_\psi=J_0(T_0-\bar t),\quad
\bar t=\langle J_0T_0\rangle,\quad
\delta=|\bar t|<1,\quad \langle J_0\rangle=1,
$$
则 $A$ 本身闭合且正则。取 $\Gamma=A$，新周长因子满足
$$
1-\delta^2\le L=\langle J_0|T_0-\bar t|\rangle
 \le\sqrt{1-\delta^2}. \tag{3}
$$
下界用 $|T_0-\bar t|\ge T_0\cdot(T_0-\bar t)$；上界用均方及
$\langle J_0|T_0-\bar t|^2\rangle=1-\delta^2$。因此
$$
|J/J_0-1|\le\delta/(1-\delta).
$$
若旧物理圈为 $C_0+rA$，令新 $C=C_0+r\langle AJ\rangle$ 保持真实弧长重心，同 $\psi$ 对应的位置改量准确为
$$
r(L^{-1}-1)(A-\langle AJ\rangle),
$$
是二阶 $\delta^2$ 尺度的缩放。

对实际有限插值原函数，须先支付
$\varepsilon=\|A_\psi/J_0-(T_0-\bar t)\|_\infty$；(3) 的下、上界分别再减、加 $\varepsilon$，正则性需 $1-\delta-\varepsilon>0$。其余量使用真实 $A_\psi$。R703 末 $\delta\approx.001652$ 仅为已付样本，不能直接代全圈证书。同 $\psi$ 的小位置改量也不控制同材料 $\phi$ 的径二 jet，后继须分别反求 $\Psi_0,\Psi$ 并记录全部六项实物改变、中心左右迹和费用。改变旧插值节点数不是同一参考场。

## 7　固定材料相位与后续冻结

在 R680 的端安置特例，令
$$
F_\alpha(r,\phi)=R_z(\alpha)F(r,\phi-\alpha).
$$
每点须先按同一旧 $\Psi(r,\phi-\alpha)$ 求逆，之后施刚转。外圈标签准确固定。内圈中心为 $R_z(\alpha)C_i$，内刚件的转动为
$$
H_\alpha=R_z(\alpha)Q R_z(-\alpha)Q^{-1},
$$
并配相应真实中心平移。两端全部材料 jet 相接。若基相位对一条具体 $E$ 的整圆误差至多 $\eta$，所有 $\alpha$ 共用此 $E$、同一上界；真等距时才得到真实同度量族。固定内握柄须对全形体再施内刚件变换的逆。

R680 的全像支撑差、握持和法管仍要求这同一个实物环带满足其全部条件。选定一条具体 $E_*$ 后，系数、材料 $r$、端实现必须冻结；后续所有参数升阶、独立读出和精化都使用同一 $E_*$。不同时间各自最优 $E$，或每次角加密重求目标均值，都不是固定 $g$ 的精化。本条不复跑 R703 的旧矩阵，不授 R718 未观察资格，课题仍未完成。
