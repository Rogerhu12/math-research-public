# 显式直纹端口六秩稿：完整独立审查

2026-11-10；Astra-visible-flex-78718bd0 / independent_audit。

**结论：原稿全部六节的初态、符号、六秩和局部控制引理通过完整独立审查。**
本审者未参与作者的曲线选择或行列式探索，未参与本题主 M14 数值候选优化。
已用另一种列构造及完整 Leibniz 求和独立复算准确行列式，也实际重跑了冻结原脚本。
没有发现阻断上述引理的缺口。配套完整环带族及其定量几何仍须另作全文审查。

## 1. 冻结对象与本轮真实执行

全文审查 notes/2026-11-10-78718-root-ruled-port-rank.md，
6135 字节，SHA256
b843f172f596aaf173d50eea007a55aed7dae5f9f46af237b89c090a9c61bc14。

冻结作者脚本 scripts/78718-check-ruled-port-rank.py，
3253 字节，SHA256
752636eab24bfea1fa0f2bcbaa4fbf408a27218af3ab365ba497d59471b7670d。

本审者另写独立程序
notes/2026-11-10-78718-audit-ruled-port-rank-recompute.py，
3774 字节，SHA256
fdeb0bbeecb3abb9b85d4fd5b6aff179766f9c2a782998bd469cb4674b80eeef。
它不导入作者程序，不用 Gaussian 消元；先以向量三重积构造列，再作全部
720 项整数 Leibniz 求和。

实际独立运行如下，两次均在当前仓库根目录启动 fresh Python 进程：

- 原冻结脚本：工具回执 130cd1，正常退出 0，PASS_EXACT_SIX_COLUMN_RANK_ONLY。
  输出 notes/2026-11-10-78718-audit-ruled-port-original-replay.json，
  711 字节，SHA256
  cea200fb30287df84d815167d50739324ebb0fa8b9a7ac3a1045d488376ece4a。
  该确定性输出与作者输出相同，但本记录的执行证据是本次实际工具退出，不是复制原文件。
- 独立 Leibniz 程序：工具回执 244f32，正常退出 0，
  PASS_INDEPENDENT_EXACT_LEIBNIZ_RANK，720 项，rank=6。
  输出 notes/2026-11-10-78718-audit-ruled-port-leibniz-replay.json，
  919 字节，SHA256
  4d6c8ecaa8bde7d264834b77dda33943134dcebdf7835e998619d3b15af74b4a。

数组没有进入对话。两次只做精确代数，ODE、PDE、优化和几何网格运行数均为 0。
行列式之外的初态、变分和局部化论证由下面完整纸面证明支付。

## 2. 初态是同一条真正解析闭嵌入曲线

记 $A=\gamma_v$、$B=\gamma_{vv}$、$s=|A|$，其中

$$
\gamma=(c,b,\epsilon(c^2-b^2)),\qquad
A=(-b,c,z_v),\qquad B=(-c,-b,z_{vv}),\qquad \epsilon=1/10.
$$

$c=\cos v,b=\sin v$。水平投影是单位圆，故不同材料角对应不同空间点；
$s^2=1+z_v^2\ge1$，所以曲线正则、闭合且嵌入。
真实弧长 $u(v)$ 的导数为正的解析函数 s，故其局部逆也解析；
$u(v+2\pi)=u(v)+\ell$。所有以下对象确实是同一弧长圆周上的解析周期函数。

因为 $A\cdot B=z_vz_{vv}$，

$$
D=s^2B-(A\cdot B)A=(A\times B)\times A.
$$

特别 z 分量是 $(1+z_v^2)z_{vv}-z_v^2z_{vv}=z_{vv}$，
其余两分量恰为原稿所列式。于是

$$
D\cdot A=0,\qquad D\cdot(c,b,0)=-s^2<0.
$$

D 从不为零。又 $D\perp A\times D$，且

$$
|D+A\times D|^2=|D|^2(1+s^2)>0.
$$

所以 W、d 的定义在全圈合法，d 是真正解析周期单位法向场。

直接对 $T=A/s$ 按 u 微分得到

$$
T_u=\frac{D}{s^4},\qquad k_F=\frac{|D|}{s^4}>0.
$$

因而 Frenet 法向和副法向在全圈都无奇点，并分别为
$n_F=D/|D|$、$b_F=(A\times D)/(s|D|)$。由此准确得到

$$
d=\frac{n_F+s b_F}{\sqrt{1+s^2}}.
$$

这里没有把 v 误当作弧长，曲率公式中的 $s^4$ 是必要的。

## 3. 倾斜后的三个符号

置 $\theta=\arctan s$，则
$d=\cos\theta\,n_F+\sin\theta\,b_F$，且

$$
N=d\times T=\sin\theta\,n_F-\cos\theta\,b_F.
$$

所以 $(d,T,N)$ 具有正定向。由 $d\cdot T=0$ 得

$$
\alpha=d_u\cdot T=-d\cdot T_u
=-\frac{k_F}{\sqrt{1+s^2}}<0,
$$

而

$$
C_0=T_u\cdot N
=\frac{k_Fs}{\sqrt{1+s^2}}>0.
$$

由 Frenet 方程
$(n_F)_u=-k_FT+\tau_Fb_F$、$(b_F)_u=-\tau_Fn_F$，进一步直接计算

$$
d_u=-k_F\cos\theta\,T
-(\theta_u+\tau_F)\sin\theta\,n_F
+(\theta_u+\tau_F)\cos\theta\,b_F.
$$

与 N 配对给 $\beta=-(\theta_u+\tau_F)$，原稿符号正确。
所有这些结论是全角严格结论，不只是在六个取样点成立。
紧圆周也给 $-\alpha$ 和 $C_0$ 各自的正最小值，但本引理不预先声称任何指定数值。

## 4. 完整 SE(3) 导数及一个不同的向量推导

令 $R=(d,T,N)$。原稿标架方程准确等价于

$$
R_u=R\widehat\omega,\qquad
\omega=(C,-\beta,\alpha),\qquad
\gamma_u=Re_2,
$$

其中

$$
\widehat\omega=
\begin{pmatrix}
0&-\alpha&-\beta\\
\alpha&0&-C\\
\beta&C&0
\end{pmatrix}.
$$

因此在 $G=(R,\gamma)$ 的齐次坐标表示中，
$G_u=G\xi$，$\xi=(\widehat\omega,e_2)$。
只改变 C 为 $C_0+\varepsilon f$ 时，$\delta\xi=(f\widehat e_1,0)$。

固定初值后，置 $H=\delta G\,G^{-1}$。微分时
$\delta G\,\xi G^{-1}$ 与来自 $(G^{-1})_u$ 的项相消，故

$$
H_u=G\,\delta\xi\,G^{-1},\qquad H(0)=0.
$$

SE(3) 的共轭在旋转/平移向量表示下为

$$
\operatorname{Ad}_{(R,\gamma)}(\omega,v)
=(R\omega,\gamma\times R\omega+Rv).
$$

所以端点导数确为

$$
\int_0^\ell f(u)\binom{d(u)}{\gamma(u)\times d(u)}\,du.
\tag{D1}
$$

再用普通向量变分独立核一次平移符号。令
$\delta R\,R^T=\widehat\Omega$，则 $\Omega_u=f d$，
$\delta T=\Omega\times T$。由 $\delta\gamma_u=\Omega\times\gamma_u$ 积分分部得

$$
\delta\gamma(\ell)
=\Omega(\ell)\times\gamma(\ell)
+\int_0^\ell f\,\gamma\times d\,du.
$$

右平凡化的平移坐标是
$\delta\gamma(\ell)-\Omega(\ell)\times\gamma(\ell)$，因此恰为 (D1) 下三项。
只积分 d 会遗漏全部平移闭合；原稿没有这个遗漏。

基态 $G(\ell)=G(0)$，故可选实际六维端点方程
$\log(G_C(\ell)G(0)^{-1})=0$，在单位元附近取 SE(3) 的局部对数坐标。
它的导数就是 (D1)。更换固定初值、基点或合法局部坐标仅施加可逆线性映射，
不影响满秩。

## 5. 六点精确行列式的独立重算

点值列 $\Phi=(d,\gamma\times d)^T$ 乘正数 $|W|$ 就是
$\mathcal P=(W,\gamma\times W)^T$。
因此六列 $\mathcal P$ 可逆与六列 $\Phi$ 可逆严格等价。

独立计算没有调用原稿展开的 D 分量。使用

$$
H=A\times B,\qquad D=H\times A,\qquad
W=D+s^2H,
$$

最后一个等式来自 $A\times D=s^2(A\times B)$。
这是与原作者脚本不同的列构造。

对题中六个有理 $(c,b)$ 点，以有理数计算每列。
取各列分母的正最小公倍数 $m_j$，将该列乘以 $m_j$ 得整数矩阵 B。
对它直接执行全部 720 项

$$
\det B=\sum_{\pi\in S_6}
(-1)^{\operatorname{inv}\pi}\prod_{i=1}^6 B_{i,\pi(i)}.
$$

再除以 $\prod_jm_j$；全程仅整数及 Fraction 运算，没有浮点或消元主元选择。
程序还分别累计正项和负项绝对值，回执保存这两个整数及其差，便于独立重放。

实际结果与原稿一致：

$$
\det[\mathcal P(v_1)\ \cdots\ \mathcal P(v_6)]
=
\frac{15838112388562926448768487424}
{9876209658570587635040283203125}>0.
\tag{D2}
$$

冻结作者脚本的消元也已真实重跑通过。其每次主元交换变号、主元乘积和
仅更新剩余子块的算法正确；非零主元不存在时返回零也符合行列式定义。
两份算法的正确性和实际执行共同核清 (D2)，不是把源码存在当作运行。

## 6. 从点值满秩到任意开弧中的真实控制

$\Phi(u)$ 和 $\mathcal P(u)$ 都全圈实解析。
假如某个非空开弧 J 上的点值只张成真子空间，取该子空间的非零实线性
消去泛函 q，则 $q\mathcal P(u)=0$ 在 J 上恒成立。
实解析恒等定理在连通的弧长圆周上延拓该恒等式，与 (D2) 矛盾。
所以每个 J 上的张成空间都是整个六维空间。

从中逐次选取增加秩的点值，能选出六个不同点。有限个不同点之间以及到
较小工作弧边界之间有正间距，故可以取互不相交的光滑窄 bump。
bump 要以真实弧长 du 归一为单位积分；这样其六个 (D1) 列趋于真实点值列，
不产生遗漏的 s 因子。行列式连续且极限非零，故充分窄时积分矩阵可逆。

要同时保留自由 bump，可先在 J 内选两个闭包互不相交的非空子弧：
六个控制全放在第一个子弧，非零自由 bump 放在第二个子弧。
前一段解析张成结论保证这样做仍有满秩，不会因预留自由支撑而失去六个控制方向。

## 7. 有限维隐函数定理与固定末段

写

$$
C_{\tau,a}=C_0+\tau f_0+\sum_{j=1}^6 a_jf_j.
$$

标架 ODE 的旋转系数反对称，保持 SO(3)，平移速度恒为单位向量；
在固定有限弧长区间上解真实存在并光滑依赖全部有限参数。
六维端点映射在原点为零，对 a 的 Jacobian 正是上一节的可逆积分矩阵。
有限维隐函数定理给 $a=a(\tau)$，使旋转和位置端点同时精确闭合，
不只消去一阶误差。

自由 bump 与控制支撑不交，因此在其支撑上准确有
$C_{\tau,a(\tau)}-C_0=\tau f_0$，非零参数不可能被控制完全抵消。
这支付材料第二形式的非平凡变化；完整集合意义的非全等仍由配套稿另证。

若选 J 为一个避开基点的真开弧，所有扰动支撑紧含于其中，则 J 前面的
解由同初值、同方程唯一性固定。J 后面的解不能只由这句话断言固定：
完整端点闭合先给共同末值，再在系数相同的末段从终点向后解 ODE，
才得到该末段的框架和曲线也精确固定。
原稿最后一段明确使用了这两步，逻辑正确。
这证明 J 外的开弧可固定，而不额外声称 J 内各个控制支撑之间的空隙都固定。

## 8. 共同直纹度量及嵌入结论的准确读法

由 $F=\gamma+rd$，直接有

$$
F_r=d,\qquad F_u=(1+r\alpha)T+r\beta N.
$$

故 $F_r\cdot F_u=0,|F_r|=1$，且

$$
g_{uu}=(1+r\alpha)^2+r^2\beta^2
$$

严格不含 C；弧长周期 $\ell$ 也没有随参数改变。
$r=0$ 的曲面法向按 $(r,u)$ 定向为 $d\times T=N$，
因此第二形式的角向系数确为 C，混合系数为 $\beta$、径向系数为零。
还应区分 $(g_{uu})_r(0)=2\alpha<0$ 与角向长度因子导数
$a_r(0)=\alpha<0$，原稿没有混淆这两个量。

共同度量公式对任意真实解都成立；末尾“足够小宽度保持嵌入”应按本文语境
理解为原闭嵌入种子及其 IFT 小参数解族，而不是对任意大的控制函数声称嵌入。
这一准确局部结论可以直接证明：在种子曲线处 d 与 T 独立，紧性给统一的
局部嵌入窗口；相隔固定材料距离的曲线点有正距离，取窄直纹宽度排除远点重合。
再将参数限制到足够小的固定紧区间，解的 C¹ 连续依赖保持这些局部和远点余量。

本引理没有给这个窗口的有效数值，也没有给整个环带的可见幅度、目标 reach、
全欧氏商非全等或帽封闭。本次审查不替配套稿预付这些几何门。
材料角端点闭合只得到一个带两条径向边界的环带，不能称闭曲面。

## 9. 审查结论和后续边界

接受同一明确闭嵌入种子、倾斜法向的全角严格符号、完整六维端点导数满秩、
任意开弧控制局部化及上述局部有限维隐函数定理。
没有使用数值通用秩、样本正性或只旋转闭合作替代。

配套实际族稿将另外审查固定宽度、全部点对的嵌入/reach、固定 H、严格收缩、
完整像非全等及相应常数。此处所有工作与主 M14 参数选择无关，
最终原始种子独立数值重跑的资格保持。
