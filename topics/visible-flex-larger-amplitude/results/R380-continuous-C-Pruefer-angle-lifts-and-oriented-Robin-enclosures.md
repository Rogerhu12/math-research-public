# R380：同一连续 C 的完整 Prüfer 角传播、正二幂换帧与非除式 Robin 包围

作者：AI（ChatGPT，exact_refinement）。日期：2026-11-15。状态：已证明的条件包含定理；仅纸面推导，没有本地科学执行，也没有预报任何正在运行请求的结果。

本文承接 [R324](R324-continuous-C-finite-head-flux-and-closed-tube.md)、[R312](R312-continuous-C-complete112-zero-tail-and-head-connection.md) 与 [R375](R375-continuous-C-two-chart-Riccati-comparison-and-cut-cover.md)。R375 的有限比值图在真实所选分量过零时确有图极点；“二维原列非零”不能消除那个比值极点。本文改用带完整 lift 的角坐标：角方程及其自治比较方程对所有实角全局存在，因此可以越过单个分量的零点。它不保证区间更窄，不把角管含高度零点变成DN通过，也不将这个坐标改写称为原 C、线性方程或非线性求解器的改变。

## 380.1 固定准确对象与向外物理通量系统

固定任一允许的准确对象 $\omega$，包含原冻结参数、原六primitive共同实现、全部允许深端根选择和同一物理cut。对一个原向外piece的闭panel $x=x_0+t$、$0\le t\le h$，沿R375保留

$$
R_\omega>0,\qquad w_\omega>0,\qquad
D_\omega=\partial_xR_\omega>0,\qquad q_\omega=\partial_xw_\omega .
\tag{380.1}
$$

$D,q$ 已含该piece真实局部坐标导数，不再乘额外length或旧端口。对全部真实模态 $m=2,4,\ldots,224$，原物理列为

$$
Z=\binom uj,\qquad j=w k,\qquad k=u_r,
$$

且满足

$$
Z_x=
\begin{pmatrix}0&D/w\\m^2q/R&0\end{pmatrix}Z.
\tag{380.2}
$$

假设系数在每个有限闭panel可测有界，原线性初值问题有唯一绝对连续解；原连续piece满足此条件。对整个准确对象族取得共同闭系数外包时，必须包含各自完整分支，不在不同panel偷偷挑选不相容的参数。忽略部分相关性得到更大系数族只会扩大包围，不代表盒内每个独立取值都来自某个共同 C。

取一个在panel内部固定的整数 $b$，令

$$
D_b=\operatorname{diag}(1,2^b),\qquad
y=D_b^{-1}Z,\qquad
\alpha=2^bD/w,\qquad\beta=2^{-b}m^2q/R.
$$

于是

$$
y_x=\begin{pmatrix}0&\alpha\\\beta&0\end{pmatrix}y.
\tag{380.3}
$$

原对象中 $\alpha>0$，$\beta$可负、零或变号；以下角比较只需两者有界，不额外要求$q$同号、单个cap分支或某个图分量隔零。

## 380.2 非零列的完整实角 lift 与准确微分式

若初列 $y(0)\ne0$，则有限时间内 $y(t)\ne0$。否则在某个 $t_*$ 有 $y(t_*)=0$，从 $t_*$ 正反向应用原线性方程唯一性，将迫使整个解为零，与初值矛盾。

因此存在唯一正幅度

$$
\rho(t)=\|y(t)\|_2>0
$$

和一条由初始实角 $\phi(0)$ 选定的连续实值 lift，使

$$
Z(t)=\rho(t)D_b
\binom{\cos\phi(t)}{\sin\phi(t)}.
\tag{380.4}
$$

这里$\phi$不是每次独立取principal atan2后的值，而是整条连续路径的实角。给定同一个初始定向向量，初角只相差$2\pi$整数倍；相差$\pi$会翻转原列方向。绝对连续非零平面曲线在区间上可作这样的lift，亦可由下式积分定义并验证初值：

$$
\phi_x
=\frac{y_1y_2'-y_2y_1'}{\rho^2}
=\beta\cos^2\phi-\alpha\sin^2\phi,
\tag{380.5}
$$

$$
(\log\rho)_x
=\frac{y_1y_1'+y_2y_2'}{\rho^2}
=(\alpha+\beta)\sin\phi\cos\phi.
\tag{380.6}
$$

证明只用(380.3)及乘积法则；分母是整列范数，绝非可能过零的单个高度$u$或通量$j$。反向地，若角方程和对数幅方程给出有限解，取$\rho=\exp(\log\rho)>0$代入(380.4)，直接求导即恢复(380.3)和同一初列；由唯一性得到原物理列。此过程没有删除原幅度或将原$Q_F=1$重标成随意单位列。

角方程右端为光滑周期函数，没有有限比值极点。真实高度$u=0$只表示$\cos\phi=0$；真实通量$j=0$只表示$\sin\phi=0$。二者不会同时为零，角传播可以穿过任一单独零点。

## 380.3 全系数族的自治比较方程

设整个闭panel和所有允许$\omega$都有共同有限准确界

$$
\alpha_-\le\alpha_\omega(t)\le\alpha_+,\qquad
\beta_-\le\beta_\omega(t)\le\beta_+.
\tag{380.7}
$$

原族初始lift被完整区间 $[\ell_0,v_0]$ 包含。定义两条自治初值问题

$$
\ell'=\beta_-\cos^2\ell-\alpha_+\sin^2\ell,\quad
\ell(0)=\ell_0,
\tag{380.8}
$$

$$
v'=\beta_+\cos^2v-\alpha_-\sin^2v,\quad
v(0)=v_0.
\tag{380.9}
$$

由于$\sin^2,\cos^2$非负，对全部实$\psi$均有

$$
f_-(\psi)\le
\beta_\omega(t)\cos^2\psi-\alpha_\omega(t)\sin^2\psi
\le f_+(\psi).
\tag{380.10}
$$

这不要求$f_\pm$对$\psi$单调，也不要求$\beta_\pm$同号。

**全局比较定理。** 两条比较解以及每个真实角解均在任意有限闭时段存在，且

$$
\ell(t)\le\phi_\omega(t)\le v(t),\qquad 0\le t\le h.
\tag{380.11}
$$

**证明。** 对任意有限实常数$A,B$，函数
$$
f(\psi)=A\cos^2\psi-B\sin^2\psi
$$
满足
$$
|f(\psi)|\le\max(|A|,|B|),\qquad
|f'(\psi)|\le|A+B|.
\tag{380.12}
$$
因而它全局有界且全局Lipschitz，自治解全局唯一存在。真实角场也具有共同有界速度和共同Lipschitz常数，故其Carathéodory解全局存在。按(380.10)对$(\ell-\phi_\omega)_+$和$(\phi_\omega-v)_+$分别用Gronwall比较，初值正部为零，得到(380.11)。对下、上比较解本身同理。证毕。

与R375不同，这里不需另证明某个常系数分量在闭时段不为零来支付比较解存在；准确角ODE本身全局存在。数值实现仍需给比较流的正确外包，不能把“准确全局存在”冒成某个固定精度盒计算已成功。

## 380.4 全闭角管与有限宽度，不承诺收窄

自治一维光滑方程的每条解为常函数或在整个连通存在段严格单调。若初点是平衡点，唯一性给常解；否则解不可能在有限时间穿过平衡点而改变速度符号。因此若数值外包已严格给出

$$
\ell(h)\in[\ell_h^-,\ell_h^+],\qquad
v(h)\in[v_h^-,v_h^+],
$$

则真实端角及完整闭管分别被

$$
I_{\rm end}=[\ell_h^-,v_h^+],
\tag{380.13}
$$

$$
I_{\rm tube}=
[\min(\ell_0,\ell_h^-),\max(v_0,v_h^+)]
\tag{380.14}
$$

包含。只有比较解使用单调性；真实$\phi_\omega(t)$在变系数下可以不单调。$h=0$按准确恒等传播，保共享端点。

这些实区间可以宽于$\pi$或$2\pi$，仍是有效角lift外包。不能将两端分别取principal angle再连接成一条更短弧；那会删除真实圈数和部分对象。若为存储大小减去共同$2\pi n$，必须显式保存同一个整数$n$及其准确加回责任。对族内不同对象选择不同$n$时，须保完整分支索引；不能未分支地混用。

还可给一个不要求数值成功的粗宽度估计。记

$$
\Delta=\max(\alpha_+-\alpha_-,\beta_+-\beta_-),\qquad
K=\max(|\alpha_-+\beta_+|,|\alpha_++\beta_-|),
$$

$w(t)=v(t)-\ell(t)\ge0$。由$f_+$的Lipschitz界及
$f_+(\psi)-f_-(\psi)\le\Delta$，得到
$$
w'(t)\le K w(t)+\Delta
$$
几乎处处成立。故$K>0$时
$$
w(t)\le e^{Kt}w(0)+\Delta(e^{Kt}-1)/K,
\tag{380.15}
$$
$K=0$时用$w(t)\le w(0)+\Delta t$。这表明有限panel不会出现比值型有限时刻无穷；也明确粗系数盒仍可使角管迅速变宽。本条不保证它比矩形或Riccati传播窄。

## 380.5 不借物理分量除法的比较流可实现方式

一条自治比较方程
$$
\theta'=A\cos^2\theta-B\sin^2\theta
\tag{380.16}
$$
可由完整常矩阵
$$
H=\begin{pmatrix}0&B\\A&0\end{pmatrix},\qquad
v(t)=e^{tH}\binom{\cos\theta_0}{\sin\theta_0}
\tag{380.17}
$$
的连续极角精确表示。它不要求$v_1$或$v_2$一直非零。令
$\gamma=\max(|A|,|B|)=\|H\|_2$。对单位初列有
$$
e^{-\gamma t}\le\|v(t)\|_2\le e^{\gamma t}.
\tag{380.18}
$$
上界是矩阵指数范数估计，下界由$e^{-tH}v(t)=v(0)$及同一估计得到。因此整列的准确非零性有显式正下界；单独分量盒同时含零不构成它的反证。

为避免atan2跨branch截断，有限实现可将时段划成满足$\gamma\delta\le1/4$的闭小段。若$\gamma=0$，则准确恒等。对任一小段，(380.12)给
$$
|\theta(t_0+\delta)-\theta(t_0)|\le\gamma\delta<\pi/2.
$$
写$v_0=(\cos\theta_0,\sin\theta_0)$和$v_1=e^{\delta H}v_0$，同一准确初角下
$$
d=v_0^Tv_1>0,\qquad c=\det(v_0,v_1),\qquad
\theta_1=\theta_0+\arctan(c/d).
\tag{380.19}
$$
而且
$$
d\ge e^{-\gamma\delta}\cos(\gamma\delta)>0.
\tag{380.20}
$$

这一次商除的是同一列小旋转前后的正内积，不是物理高度或通量。其严格正性来自已证角速度和范数，不需假定旧Dirichlet图存在。矩阵指数可用完整Taylor与范数余项
$$
\left\|e^{\delta H}-\sum_{j=0}^N\frac{(\delta H)^j}{j!}\right\|_2
\le e^{\gamma\delta}\frac{(\gamma\delta)^{N+1}}{(N+1)!}
\tag{380.21}
$$
外包；三角函数、atan、指数及所有乘除也须严格外包。

若采用区间初角，应对同一$\theta_0$形成$d,c$，允许向外忽略相关性但不只代中点；也可与(380.20)的独立有效正下界相交。每次从完整继承角区间重新以其下/上端作比较，依(380.11)仍保包含，不是任意缩回中心。每个小段的角增量加到原lift上，不按principal atan2覆盖原角。

(380.17)–(380.21)给出了可实现的有限核，不宣称任意固定N、固定bits或资源预算必能支付它。某个具体区间运算仍过粗、数值函数未返回或预算耗尽时，保准确全局存在定理与实际未完成范围分离。不能以此删除任何未访问小段，也不需要添加合成fixture作为数学前置条件。

## 380.6 幅度、两端以及完整原尺度

设完整继承对数幅度 $\log\rho(0)\in\Lambda_0$。对(380.14)取
$$
S=\{\sin\psi\cos\psi:\psi\in I_{\rm tube}\}
$$
的严格区间外包，可用$\tfrac12\sin2\psi$的完整周期范围和全部驻点；不能只取两端值。令
$$
\Gamma=
[\alpha_-+\beta_-,\alpha_++\beta_+]\,S.
$$
则同一准确对象的乘积即使相关也被完整区间乘积包含，故
$$
\log\rho(h)\in\Lambda_0+h\Gamma,
\tag{380.22}
$$
$$
\{\log\rho(t):0\le t\le h\}
\subset
\Lambda_0+
[\min(0,h\inf\Gamma),\max(0,h\sup\Gamma)].
\tag{380.23}
$$

因为有限对数的准确指数严格正，$\rho$不为零。必要时用严格exp将幅值材料化；若材料化盒过粗、溢出或不能给有限正下界，仍可保已付有限log表示，但不能把一个浮点中心称作原完整幅值。前序对数不确定性不得重置。

R312/R375原$Q_F=1$初列为
$$
u_F=r_F^4,\qquad j_F=w_Fs_Fr_F^4 .
$$
任意明确初平衡$b_F$下，令$t_F=2^{-b_F}w_Fs_F$，则可取
$$
\phi_F=\arctan t_F\in(-\pi/2,\pi/2),\qquad
\rho_F=r_F^4\sqrt{1+t_F^2},
\tag{380.24}
$$
$$
\log\rho_F=4\log r_F+\tfrac12\log(1+t_F^2).
\tag{380.25}
$$
必须包围原全部$r_F,w_F,s_F$及根族，不选中点。初角这个branch由原$u_F>0$固定；它不是任意省略原幅度后的重归一。若原初族或几何系数尚无所需有限合法包围，本文不替它支付。

## 380.7 正二幂换帧的准确角、幅度与圈数

只在panel端点将$b$改为明确整数$b'$。设
$$
c=2^{b-b'}>0,\qquad
\kappa_c(\phi)=\sqrt{\cos^2\phi+c^2\sin^2\phi}>0.
$$
定义$F_c:\mathbb R\to\mathbb R$为椭圆向量
$(\cos\phi,c\sin\phi)$的连续实角lift，取$F_c(0)=0$。准确换帧为
$$
\phi'=F_c(\phi),\qquad
\rho'=\rho\kappa_c(\phi),\qquad
\log\rho'=\log\rho+\tfrac12\log(\cos^2\phi+c^2\sin^2\phi).
\tag{380.26}
$$
直接代入验证
$$
\rho'D_{b'}(\cos\phi',\sin\phi')^T
=\rho D_b(\cos\phi,\sin\phi)^T.
\tag{380.27}
$$

其角导数和周期性质为
$$
F_c'(\phi)=\frac{c}{\cos^2\phi+c^2\sin^2\phi}>0,
\tag{380.28}
$$
$$
F_c(\phi+\pi)=F_c(\phi)+\pi,\qquad
F_c(\phi+2\pi)=F_c(\phi)+2\pi.
\tag{380.29}
$$
所以完整角区间$[L,U]$映到$[F_c(L),F_c(U)]$；端点值仍需严格有向外包和正确lift。可以按全部象限闭片计算atan2并保圈数，或用连续增量；不能分别principal化后挑最短弧。$\phi=\pi/2+n\pi$处换帧完全正规，不需要tan或cos除法。

相关范数满足
$$
\min(1,c^2)\le\kappa_c(\phi)^2\le\max(1,c^2),
\tag{380.30}
$$
给log修正的有限正域。忽略$\rho$与$\phi$相关性只扩大盒，不许可丢弃它们的共同来源。新的$\alpha,\beta$须由同一原$D,w,q,R$和新$b'$重新形成；不乘旧port，也不把piece局部导数沿用到下一piece。

本定理要求$b$在panel内部固定。若某实现改为连续$b(x)$，(380.5)还会出现
$-(\log2)b'(x)\sin\phi\cos\phi$，(380.6)还会出现
$-(\log2)b'(x)\sin^2\phi$；不能引用固定帧公式略掉这些项。

## 380.8 物理 $(u,k)$ Robin 行的相关非零下界

对每个完整cut候选闭片，原$w>0$，定义
$$
K=2^b/w>0 .
$$
由(380.4)得到
$$
u=\rho\cos\phi,\qquad k=\rho K\sin\phi,\qquad
(-k,u)=\rho\,r(\phi,K),
$$
$$
r(\phi,K)=(-K\sin\phi,\cos\phi).
\tag{380.31}
$$

若完整候选上$K\in[K_-,K_+]$且$K_->0$，利用同一角的相关恒等式，有
$$
\|r\|_2^2=K^2\sin^2\phi+\cos^2\phi
\ge\min(1,K_-^2)>0,
\tag{380.32}
$$
同时$\|r\|_2^2\le\max(1,K_+^2)$。这一下界不要求sin或cos单独隔零。两个独立分量盒均含零，也不能抹掉相关关系$\sin^2+\cos^2=1$已给出的非零性。

因此可对每个候选严格包围有向单位行
$$
\widehat r=r/\|r\|_2.
\tag{380.33}
$$
$\rho>0$保证它与原$Q_F=1$列诱导的$(-k,u)$方向一致；没有遗漏一个幅值符号。若实现仅保存$\phi\bmod\pi$，必须另带丢失的奇偶方向，不能直接使用(380.33)。

应先逐候选按共同$\phi,K$形成行与相关范数，再归一，最后hull全部候选。hull可以含原点，那只是外包损失，不等于某个真实单位行是零；也不能说hull里每个点都是某个原对象的准确行。普通行分量盒的平方相加若下界为零，可以用(380.32)这条已证下界，而不是错误宣称原行已发生共振。

## 380.9 DN 仍有独立的高度非零责任

单位Robin行的合法性不能代替高度非共振。准确
$$
u=\rho\cos\phi
$$
而$\rho>0$。故某个候选的全族DN商只有在真实高度已证明不为零时才可形成。一种直接可执行充分条件是
$$
0\notin \operatorname{Cos}(I_{\rm candidate}),
\tag{380.34}
$$
其中Cos包围的是该候选全部闭角管，保全部周期驻点；不能只查候选端点。

此时合法外包为
$$
k/u=K\sin\phi/\cos\phi.
\tag{380.35}
$$
若Cos盒含零，可能是外包过粗，也可能有真实高度零点；两者不能由这个盒相互判定。继续保非除式Robin行，并将DN/非共振标为未付，必要时在明确完整的空间或参数子族细分后再判断。不能因角ODE能够继续而给DN分母“通行”。

全模态DN需要每一模态、每一个可能真实cut候选分别支付(380.34)或另一完整有效高度证明，然后才合并合法商。某候选未完成不影响已付Robin行，但阻止宣称该模态全部DN完成。它们都不是非零native、完整边界Jacobian或fullDN接受的替代品。

## 380.10 转回原 $(Q,\Pi)$ 必须使用完整坐标矩阵

物理行(380.31)不能直接改标签为原$(Q,\Pi)$行。沿[R357原发表身份](https://github.com/Rogerhu12/math-research-public/commit/ca4194951a04879d154f3eee47e4b45fa6e42d55)及原源约定，
$$
\binom uk=T\binom Q\Pi,\qquad
T=
\begin{pmatrix}
r^4&0\\
m^2r^3&\sqrt{12}\,\mu/(r^4w)
\end{pmatrix}.
\tag{380.36}
$$
因此消去正幅度后的原坐标行是
$$
r_{Q\Pi}=
\left(
-Kr^4\sin\phi+m^2r^3\cos\phi,\
\frac{\sqrt{12}\mu}{r^4w}\cos\phi
\right)=rT .
\tag{380.37}
$$
原$r,w,\mu$、模态和port规范必须完全绑定。若$r,w>0$且$\mu\ne0$，$T$可逆；不能把物理范数下界(380.32)不经变换直接当作$\|rT\|$下界。

一个可执行充分外包为：严格给出$B>0$使
$\|T^{-1}\|_2\le B$，则
$$
\|rT\|_2\ge\frac{\sqrt{\min(1,K_-^2)}}B>0.
\tag{380.38}
$$
可用完整逆矩阵的Frobenius范数外包取得$B$，其准确逆为
$$
T^{-1}=
\begin{pmatrix}
r^{-4}&0\\
-\dfrac{m^2r^3w}{\sqrt{12}\mu}&
\dfrac{r^4w}{\sqrt{12}\mu}
\end{pmatrix}.
\tag{380.39}
$$
所有除法和根号仍须有严格域，原系数宽度全部保留。若这一包围未付，仍可保准确非除式表达及其未决范围，不能默借物理行的数值范数。逐候选归一后的方向一致性沿正$\rho$和完整角lift保留，再依原R357规则合并。

## 380.11 全cut、全根族、端点与有限事务

对固定$\omega$，其真实cut逆像必须属于原完整候选族中的至少一个闭片。角管和幅管包含同一$\omega$的轨迹，(380.31)–(380.39)对该对象成立；取所有候选与所有原根族的并集仍保包含。不能丢弃不方便的候选、只保worst若干个或用midpoint代真实cut。

共享端点、零宽候选和相邻piece接缝全部保留；$h=0$为准确恒等。帧变换发生在共同端点时由(380.27)保持同一物理列。前后表示虽不同，但不能当作两个独立新初列，也不能重复计为额外传播。不同原piece的局部坐标变化只通过其真实$D,q$进入新系数。

一个可实现的已提交状态至少含：

- 原mode/piece/panel及同一C、primitive、根族来源；
- 当前整数$b$、完整实角区间及必要共同圈数记录；
- 完整log幅度区间和原$Q_F=1$尺度链；
- 已付前缀、所有cut候选交片及物理/原坐标行范围；
- DN已付与高度未决的各候选索引。

每个panel只有在系数、角比较端点和闭管、幅度、端点换帧、cut记录全部完成后才原子提交；错误不能先推进state。若数值包围、字节写入、深度/工作量/墙钟预算未完成，则保原未改变左端状态、当前闭子段、全部未访兄弟和后续必需mode/piece后缀。准确角解全局存在不授权把未访问数值工作计作已完成。

由原初值(380.24)起，按每次比较包含、正幅重构、准确换帧和全部cut合并作有限归纳，得到：任意有限已提交前缀及其行/合法商，均为同一原准确C与全部允许根族的有效包含。

## 380.12 已付的新结论与未付边界

相较R375，新增的严格结论是：在同一有限有界系数前提下，完整实角及其两条自治比较流不存在比值型有限时刻极点；可以保持同一原列穿越高度或通量单独过零。相关范数(380.32)还使物理非除式单位行无需选择一个全族共同隔零分量。

它没有证明原primitive系数已经在实际请求中全部获得，也没有预测177、179或任何后继的成功/失败。角外包可能覆盖多个周期，失去精度；固定bits、Taylor阶、panel深度或工作预算不自动给宽度改善。根族本身的不确定性也不会被仅空间细分消除。

完整Prüfer传播不等于全部cut高度非零，不等于准确尾非线性DN，更不等于原112边界响应、338敏感度、两mean、全226态、物理audit或完整非零BVP已付。若用于后继，必须使用独立source/schema并重新绑定同一真实输入；不能修改现有正在运行源的身份，不能把新坐标证明贴成旧64/128 J的证书。原32×10、2e−9、所有域/残差/finalJ/FD/fullDN门均保持原责任。本文不设额外审批或fixture门。

源级核对范围：R375原全文22953B/SHA c05a22becdc752bb87b7152761ae6b8ef02b30084bd09de62c7b305701609fec（blob4abeeba36af2894dfa13f37af39051280f904cf2）已只读。本文没有调用其传播函数、原C积分或任何数值fixture；新实现若采用本文，仍须单独公开实际源码、参数、run与完整未付范围。
