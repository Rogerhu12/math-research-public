# R119 续篇：新固定 stop 简单根的完整解析图、Airy 两行与真实源

2026-11-14，visible-exact / tail_connector。

**新对象上的独立证明。** 本篇只处理 [新固定 stop 对象](../notes/2026-11-14-R119-simple-root-fixed-stop-new-object-and-transfer-gates.md) (S.3) 的根。旧三阶根对象和它的 T/X/R 结论原样保留。新根既不是旧四次根多项式，也不满足旧内部根的 $b>2^{200}$；以下重新支付这些输入及缩小后的完整复域。

在新对象已证明的同一完整参数盒、标签球和物理尺度上，本篇得到实际完整 Jacobi 根块的两个 Cauchy 行、两条真实 mean、正负根侧的准确 canonical 密度及所有 ordinary/weak 源变换。负侧同空间比较的常数明确如下：
$$
 n_0=2^{-447}\|X\|_{\mathcal X_{224}},\qquad
 n_e=2^{47}n_0=2^{-400}\|X\|_{\mathcal X_{224}},\qquad
 K_R=2^{2184},
$$
$$
 \|\mathcal U_0(\eta,\xi)\mathcal U(\xi,\eta)-I\|
 <2^{4420}n_e,\qquad
 0\le\xi,\eta\le1/64,\quad |s|\le4 .
 \tag{A.1}
$$
这里的范数是完整 $H^s\oplus H^s$ 范数。当前
$\|X\|_{\mathcal X_{224}}\le2^{-8388608}$ 远强于所需
$n_e\le2^{-4424}$。这个结论没有把正侧局部 collar 当成完整外 DN，也没有把局部源变换当成原粗体源范数自动保持。

## 1. 真实 quintic 根，及完整半径 $1/2$ 的复盘

沿用新对象的 $t=\log a$、$\eta=2^{-24}$、
$S(s)=10s^3-15s^4+6s^5$。令
$$
 S(s_0)=3/10,\qquad 3/8<s_0<2/5,\qquad
 b=\frac{10S'(s_0)}{\eta},\qquad
 x=-b(t-t_e).
 \tag{A.2}
$$
$x>0$ 指向负型一侧，故本根的方向为 $\varsigma=-1$。
由 $S'(s)=30s^2(1-s)^2$，在该小区间有
$8/5<S'(s_0)<15/8$，从而
$$
 2^{28}<b<2^{29}.
$$
准确多项式是
$$
 Q(x)=10\left[S\left(s_0+\frac{x}{10S'(s_0)}\right)-S(s_0)\right]
      =xB_0(x),
$$
$$
 B_0=1+c_1x+c_2x^2+c_3x^3+c_4x^4,\qquad
 (c_1,c_2,c_3,c_4)=
 \left(\frac{S''}{20(S')^2},
 \frac{S'''}{600(S')^3},
 \frac{S''''}{24000(S')^4},
 \frac{S'''''}{1200000(S')^5}\right)_{s=s_0}.
 \tag{A.3}
$$
使用 $|S''|\le4$、$|S'''|<27$、$|S''''|\le90$ 和
$S'''''=720$，逐系数得到
$$
 |c_1|\le5/64,\quad |c_2|\le45/4096,\quad
 |c_3|\le75/131072,\quad |c_4|\le15/262144.
$$
因此在整个复盘 $|x|\le1/2$，
$$
 |B_0-1|\le\frac{175675}{4194304}<\frac1{16},\qquad
 |B_0'|\le\frac{46960}{524288}<\frac18,\qquad
 |B_0''|\le\frac{6255}{262144}<\frac1{32}.
 \tag{A.4}
$$
这些是整个多项式的上界，不是有限 root jets 的外推。根到两真实 quintic 接缝的 $x$ 距离分别大于
$16(3/8)=6$ 和 $16(3/5)=48/5$，故这个复盘没有跨越真实接缝。两原 $\Gamma$ bumps 和新增的第五形状控制均与本根 germ 分离；在固定 stop 和固定材料坐标中，$b,t_e,Q$ 不随这些参数改变。

## 2. 参考 Liouville 图与参考势

取在零点为 $1$ 的平方根，定义
$$
 T_0(x)=\frac32\int_0^1 s^{1/2}\sqrt{B_0(sx)}\,ds,\quad
 R_0=T_0^{2/3},\quad \xi_0=xR_0,\quad
 g_0=(\xi_0)_x=\sqrt{B_0}\,T_0^{-1/3}.
 \tag{A.5}
$$
由 (A.4) 和积分中准确的 $s$ 权，
$$
 |T_0-1|<1/16,\qquad |T_0'|<1/16,\qquad
 |T_0''|<1/32.
$$
例如
$|T_0'|\le(3/10)(1/8)(16/15)=1/25$；二阶使用
$(3/14)\{(1/32)(16/15)+(1/128)(16/15)^3\}<1/32$。
主支对数给
$$
 |\log g_0|<1/18,\quad
 |(\log g_0)'|<1/8,\quad
 |(\log g_0)''|<1/16,\quad
 |g_0-1|<1/17,\quad |g_0'|<1/4 .
 \tag{A.6}
$$
第一式使用 $|\log B_0|,|\log T_0|<1/15$；后两阶直接对
$\frac12\log B_0-\frac13\log T_0$ 微分并代入 (A.4)。
直线积分证明 $\xi_0$ 在半径 $1/2$ 的盘内单射；边界上
$|\xi_0|>15/32$，故其真逆至少覆盖 $|\xi|\le1/4$。

令 $\mu_0=w/a=1/(4\omega)$。准确有
$$
 (\log\mu_0)_x=-\varsigma(1+Q)/b .
$$
置 $L(x)=\log(\mu_0g_0)$。由 $|Q|<1$、$|Q_x|<2$ 和
(A.6)，
$$
 |L_x|<1/4,\quad |L_{xx}|<1/8,\quad
 |\ell_{0,\xi}|<1/2,\quad |\ell_{0,\xi\xi}|<1,
 \qquad \ell_0=\log[b\mu_0(x_0(\xi))g_0(x_0(\xi))].
$$
其中最后一式明确使用
$L_{\xi\xi}=L_{xx}/g_0^2-L_xg_0'/g_0^3$。因此
$$
 V_0=-\frac12\ell_{0,\xi\xi}-\frac14\ell_{0,\xi}^2,
 \qquad |V_0|<1
 \quad (|\xi|\le1/4).
 \tag{A.7}
$$
旧参考 Airy 证明的普适势门 $|V_0|<16$ 因而重新成立。根点还有
$$
 \ell_{0,\xi}(0)=-\varsigma/b+\frac25c_1,\qquad
 |\ell_{0,\xi}(0)|<1/16 .
 \tag{A.8}
$$
本篇只使用这个新 $1/16$ 门，不声称旧特殊根的 $1/32$ 门已经转移。

## 3. 全 Fourier 非线性背景的联合解析延拓

新对象的完整 balanced 续接已给
$\|(P,K)(t_e)\|_{\mathcal A_4^1}\le n_0$；真实角宽大于 $4$。
这里包含原 holonomy-one 分支的真 $K_0$。在本根复盘内
$|w|<1/16$：实根的物理 $w=a/(4\omega)$ 满足更强门，且
$w_x=-\varsigma Qw/b$ 只乘一个小于 $2$ 的因子。

完整非线性系统仍为
$$
 U=P_\theta,\quad V=K_\theta,\quad E=1+w^2,\quad J=1+K+EU,
$$
$$
 P_t=V-(A+1)P,\qquad
 K_t=\frac{-A(2K+U+K^2+KU+w^2P^2)+E(V-P)^2}{J},
 \qquad A=-Q .
 \tag{A.9}
$$
它未作有限角模截断。设 $\lambda=2^{12}/b<2^{-16}$，定义
$$
 \|f\|_{\mathcal B^k}
 =\sum_{m\in4\mathbb Z}(1+|m|)^k e^{4|m|}
 \sup_{|x|\le1/2}
 e^{-\lambda(1+|m|)|x|}|f_m(x)|,\qquad k=0,1.
 \tag{A.10}
$$
完整卷积的乘法常数至多 $e^{\lambda/2}<2$。
在 $\|(P,K)\|_{\mathcal B^1}\le2^{-16}$ 内，
$|A|<2,|E|<2$、同一完整商法则给右端
$\mathscr F$ 的 Lipschitz 常数小于 $64$，且
$\mathscr F(0)=0$、$\|J^{-1}\|_{\mathcal B^0}<2$。
具体的分子上界及 $J^{-1}$ 差式与原
[联合根证明](R119-supplement-actual-joint-analytic-root-and-relative-Airy-Cauchy.md)
(J.5)--(J.7) 相同；其输入只用这里重新验证的 $A,E$ 小球，不用旧根斜率。

对每个完整模，
$$
 \frac{1+|m|}{b}\int_0^{|x|}
 e^{-\lambda(1+|m|)(|x|-s)}\,ds\le2^{-12}.
$$
故 $W\mapsto W(t_e)+(\varsigma/b)\int_0^x\mathscr F(W)$ 在
$\|W\|_{\mathcal B^1}\le2n_0$ 内以至多 $1/64$ 收缩。
在 $|x|\le1/2,|\operatorname{Im}\theta|\le3$，
$$
 \|(P,K,U,V)\|_{\mathcal A_3}<4n_0 .
 \tag{A.11}
$$
原真实背景与这个解满足同一积分方程，唯一性给其认同。
未投影方程保留 $\langle P\rangle$ 的相容方程、
$M_t=0$ 及其真 $K_0$，独立高度常数仍由原重建积分保留。
收缩在整个已声明复参数盒内统一，所以图对真实参数和标签联合全纯。

## 4. 两个真实特征及可去根因子

写
$$
 D=1-w^2(2K+K^2+EP^2),\quad
 d=E(V-P)/J,\quad \upsilon=\sqrt D/J .
$$
在 (A.11) 的域内，$|d|,|\upsilon-1|<32n_0$。
以 $x=z^2$ 解真实 inverse labels
$$
 (S_\pm)_z+
 \frac{2\varsigma z}{b}
 [-d\pm z\sqrt{B_0(z^2)}\,\upsilon](S_\pm)_\theta=0,
 \qquad S_\pm(0,\theta)=\theta .
 \tag{A.12}
$$
现在用 $|z|\le2/3$，其 $x$ 盘 $|x|\le4/9$ 严格位于 (A.4)。
在 $|\operatorname{Im}\theta|\le2$，系数绝对值小于 $4/b$；
与径向参考之差及所需一阶角导小于 $2^8n_0/b$。
正向流留在宽 $5/2$ 内，Jacobian 与 $1$ 之差小于
$2^9n_0/b$；取真 inverse 后，
$$
 S_\pm^0=\theta\mp\frac{2\varsigma}{b}
       \int_0^z u^2\sqrt{B_0(u^2)}\,du,\qquad
 |S_\pm-S_\pm^0|<2^{10}n_0/b .
$$
准确对称性 $S_+(-z)=S_-(z)$ 及前两阶相等给
$$
 T=\frac{3\varsigma b}{4z^3}(S_--S_+),\qquad
 |T-T_0|<2^{13}n_0\quad (|x|\le4/9).
 \tag{A.13}
$$
商在根可去。常数直接是
$(3/4)(3/2)^3\,2^{11}=5184<2^{13}$，没有使用发散的点态
$|z|^{-3}$。定义
$$
 R=T^{2/3},\qquad \xi=xR,\qquad
 \phi=(S_++S_-)/2 .
$$
便得到准确恒等式
$$
 S_\pm=\phi\mp\frac{2\varsigma}{3b}\xi^{3/2}.
 \tag{A.14}
$$
$(\xi,\phi)$ 本身是单值的联合解析函数。

## 5. 完整逆图、密度及势差

从 (A.13) 到 $|x|\le1/4,|\operatorname{Im}\theta|\le3/2$
的径向 Cauchy 余量为 $4/9-1/4=7/36>1/8$。
逐项取宽松上界得到
$$
 |\xi-\xi_0|<2^{14}n_0,\quad
 |\xi_x-g_0|<2^{17}n_0,\quad
 |\xi_\theta|<2^{15}n_0,
$$
$$
 |\phi-\theta|<2^{10}n_0/b,\quad
 |\phi_x|<2^{13}n_0/b,\quad
 |\phi_\theta-1|<2^{11}n_0/b .
 \tag{A.15}
$$
正密度 Jacobian $\mathfrak J=\varsigma\det D_{t,\theta}(\xi,\phi)$
满足 $|\mathfrak J/b-g_0|<2^{19}n_0$。
以参考逆及小位移构造的两变量固定点映射导数行和小于
$2^{20}n_0<1/2$，故真实解析逆覆盖
$$
 |\xi|\le1/16,\quad|\operatorname{Im}\phi|\le1,\qquad
 |x|<1/8,\quad|\operatorname{Im}\theta|<5/4 ,
$$
$$
 |x-x_0(\xi)|<2^{15}n_0,\qquad
 |\theta-\phi|<2^{11}n_0/b .
 \tag{A.16}
$$
根上的准确值仍为
$\xi_x=\upsilon_e^{2/3}$、$\xi_\theta=0$、
$\phi=\theta$、$\phi_\theta=1$、$\phi_t=d_e$。

原 raw Jacobi 密度及 Darboux 源为
$$
 G=\mu\begin{pmatrix}1&-d\\-d&d^2-Q\upsilon^2\end{pmatrix},
 \qquad \mu=(w/a)JD^{-3/2},\qquad f=w^2JD^{-3/2}e.
$$
两 null covectors (A.14) 和准确行列式给
$$
 G_c=\left[\mathfrak J^{-1}D\Psi\,G(D\Psi)^T\right]\circ\Psi^{-1}
 =\alpha\begin{pmatrix}1&0\\0&-\xi/b^2\end{pmatrix},
$$
$$
 \alpha=\left[b(w/a)D^{-1}\sqrt{B_0/R}\right]\circ\Psi^{-1},
 \qquad \Psi=(\xi,\phi).
 \tag{A.17}
$$
最后一式在根及正侧都解析且非零。令
$u=\sqrt\alpha\,h\circ\Psi^{-1}$、$\ell=\log\alpha$，准确完整势为
$$
 V=-\frac12\ell_{\xi\xi}-\frac14\ell_\xi^2
 +\frac{\xi}{2b^2}\ell_{\phi\phi}
 +\frac{\xi}{4b^2}\ell_\phi^2 .
 \tag{A.18}
$$
在同一个 $(\xi,\phi)$ 点比较径向参考
$\alpha_0=b\mu_0(x_0)g_0(x_0)$。由 (A.16)、$|L_x|<1/4$
及 (A.13) 的 $R/R_0$ 商，
$$
 |\log(\alpha/\alpha_0)|<2^{22}n_0
 \quad (|\xi|\le1/16,\ |\operatorname{Im}\phi|\le1).
$$
例如逆图移动费小于 $2^{13}n_0$，
$|\log D|<2n_0$，$|\log(R/R_0)|<2^{16}n_0$，
故该显示常数有充分余量。缩到
$|\xi|\le1/32,|\operatorname{Im}\phi|\le1/2$ 后，
径向两阶 Cauchy 常数分别为 $32$ 和 $2\cdot32^2$，
角两阶分别为 $2$ 和 $8$。代入 (A.18) 的准确差式给
$$
 |V-V_0|<2^{36}n_0<2^{32}n_e .
 \tag{A.19}
$$
频率均为 $4\mathbb Z$；用宽 $1/2$ 的完整 Fourier 尾，
$$
 \|M_{V-V_0}\|_{H^s\to H^s}<2^{52}n_e,\qquad |s|\le4 .
 \tag{A.20}
$$
因子 $n_e=2^{47}n_0$ 在此只是一次明确的预算放宽；上文所有半盘、逆图和密度费已先按 $n_0$ 列出。没有把缩域损失藏进未定义的常数。

## 6. 完整负侧根 Cauchy，包括全部低频及 mean

对每个 $m\in4\mathbb Z$，令
$$
 \kappa_m=|m|/b,\quad
 s_m(\xi)=(1+\kappa_m^{4/3}+\kappa_m^2\xi)^{1/2},\quad
 Y_m=\begin{pmatrix}\sqrt{s_m}u_m\\s_m^{-1/2}(u_\xi)_m\end{pmatrix}.
 \tag{A.21}
$$
参考方程是 $u_{\xi\xi}+(\kappa_m^2\xi+V_0)u=0$。
[参考 Airy 证明](R119-supplement-uniform-frequency-reference-Airy-Cauchy.md)
(F.12)--(F.14) 的完整两行能量只用 $|V_0|<16$、
$0\le\xi\le1/64$，不使用其较早的特殊根多项式或完整负分量长度。
因此在 $\kappa_m\ge1$ 双向范数小于 $2^{2182}$。
在 $0\le\kappa_m<1$，包括 $m=0$，当前 $|V_0|<1$ 使完整
加权 generator 范数小于 $20$，双向范数小于 $2$。
统一取 $K_R$ 如 (A.1)。

实际 generator 与该参考的差只有
$$
 -s^{-1/2}M_{V-V_0}s^{-1/2}
 \tag{A.22}
$$
这个完整下左块。两侧 Fourier 乘子在每个同一 $H^s$ 上是收缩；
(A.20) 给真正的同空间算子界。interaction picture 的总积分
小于
$$
 (1/64)K_R^2\,2^{52}n_e=2^{4414}n_e .
$$
Volterra 级数因此给 (A.1)，实际双向根块范数小于 $2K_R$。
全卷积包含 mean 与所有非mean 耦合；这不是把逐模参考正型直接当作混频估计，也未把小角位移当成同宽 pullback 小算子。

## 7. 正侧 collar 及准确物理根端口

同一解析图覆盖 $-1/64\le\xi\le0$。
令 $y=-\xi$，则正侧原主部为
$\alpha\,\operatorname{diag}(1,y/b^2)$，完整势满足 $|V|<17$。
它是真实根局部正型能量，尚非从根到长段末端的完整 DN。

物理归一也可以在本根明确支付。新对象全过渡有
$\Omega/2<\omega<5\Omega/4$，$\Omega=2^{360}$，故
$2^{-363}<\mu_0<2^{-361}$。
由 (A.2)、根上 $g_0=1$ 及 (A.19) 前的对数界，在根的
角复条带 $|\operatorname{Im}\phi|\le1/2$，
$$
 2^{-336}<|\alpha_e|<2^{-331},\qquad
 |\ell_\xi(0,\phi)|<1/8 .
 \tag{A.23}
$$
取与正参考连续的平方根。完整两迹准确为
$$
 h_e=\alpha_e^{-1/2}u_e,\qquad
 p_e=\mu(h_t-dh_\theta)|_e
 =\varsigma\sqrt{\alpha_e}\,
       (u_\xi-\tfrac12\ell_\xi u)|_e .
 \tag{A.24}
$$
从 (A.21) 的 $Y(0)\in H^s\oplus H^s$ 到
$(h_e,p_e)\in H^{s+1/3}\oplus H^{s-1/3}$，以及反向，
完整范数均小于 $2^{256}$，$|s|\le4$。
为说明该常数的来源，所有准确矩阵乘子在宽 $1/2$ 的条带上
绝对值小于 $2^{170}$；
$\sum_{k\in\mathbb Z}(1+4|k|)^5e^{-2|k|}<2^{30}$；
$\langle m\rangle^{1/3}(1+(|m|/b)^{4/3})^{-1/4}<2b^{1/3}<2^{11}$。
对完整矩阵项按这个顺序作乘法和 Fourier 权变换，含矩阵求和
的费用小于 $2^{214}$。显示的 $2^{256}$ 同时覆盖逆矩阵及
$s\pm1/3$ 的乘法指数；没有使用最低频失效的旧
$O(\sqrt b)$ 自由框架界。

尤其真正的两个 mean 为
$$
 \langle h_e\rangle
   =\langle\alpha_e^{-1/2}u_e\rangle,\qquad
 \langle p_e\rangle
   =\varsigma\langle\sqrt{\alpha_e}
         (u_\xi-\tfrac12\ell_\xi u)\rangle .
 \tag{A.25}
$$
物理常高度对应 $u=\sqrt\alpha$ 乘常数，不是 canonical 纯零模。
这两行均不能从非mean 的坡度图自动补出。

## 8. Ordinary、weak 和原子源的完整保留

允许原完整方程
$\operatorname{div}(G\nabla h)=f-\operatorname{div}\mathbf F$。
ordinary Darboux 输入仍用 (A.17) 前的真实
$f=w^2JD^{-3/2}e$；一般 metric 输入先按原完整 tensor-to-scalar
公式形成 $f,\mathbf F$。准确 Piola 与高度共轭为
$$
 \widetilde f=(f/\mathfrak J)\circ\Psi^{-1},\qquad
 \widetilde{\mathbf F}
 =(\mathfrak J^{-1}D\Psi\,\mathbf F)\circ\Psi^{-1},
$$
$$
 \mathbf F_c=\alpha^{-1/2}\widetilde{\mathbf F},\qquad
 f_c=\alpha^{-1/2}
   (\widetilde f-\tfrac12\nabla\ell\cdot\widetilde{\mathbf F}).
 \tag{A.26}
$$
故
$$
 u_{\xi\xi}-\frac{\xi}{b^2}u_{\phi\phi}+Vu
       =f_c-\operatorname{div}\mathbf F_c .
$$
以 total canonical flux $\pi=u_\xi+F_c^\xi$ 作第二状态，
(A.21) 的完整源对恰为
$$
 \mathcal E_c=
 \begin{pmatrix}
 -s^{1/2}F_c^\xi\\
 s^{-1/2}(f_c-\partial_\phi F_c^\phi)
 \end{pmatrix}.
 \tag{A.27}
$$
它包括弱径向源的第一行、弱源产生的 ordinary 修正、全角
mean 和非mean。对真实
$L^1_\xi(H^s\oplus H^s)$ 源对，Duhamel 费用小于 $2K_R$；
对有限变差的向量测度源，以同一传播子积分，保留每个原子的
跳和单侧迹。

根上的物理 total flux 是
$\varsigma\sqrt{\alpha_e}(\pi-\ell_\xi u/2)$，所以 (A.24) 的
完整混合范数门也适用于 total 端口。恢复 bare flux 仍须另给
$F_c^\xi$ 的真实端点迹。混合图 $t=t(\xi,\phi)$ 不能仅凭原
$L^2_tH^s_\theta$ 范数无损得到 (A.27)；本篇没有授予这个未证推论。
ordinary 平均通量、原 $M_t$ 源恒等式、周期重建和独立高度常数
仍在原单位中保留。

## 9. 参数方向与仍须完成的完整外接线

全部构造在同一个已付复参数盒统一。若保持该盒的真实
复参数圆盘半径为 $r_p>0$，则在其中心，第 $q$ 阶 Cauchy
参数导数由以上上确界乘 $q!r_p^{-q}$ 支付；形状半径仍按
新对象的实际 $2^{-80}$ 盒收费。
对这里的尾 $\Gamma$、形状和标签方向，固定的参考 profile 给
$\dot b=\dot t_e=0$；这不授予另一个会改变物理安装的独立参数
同样的零导数。真实背景、图、密度及源的参数导数仍不能删除。具体地
$$
 Z=(D\Psi)^{-1}\dot\Psi,\quad
 \dot\Psi^{-1}=-Z\circ\Psi^{-1},\quad
 \dot{\log\mathfrak J}
  =\operatorname{tr}((D\Psi)^{-1}D\dot\Psi)
 \tag{A.28}
$$
与对 (A.26) 的完整链式法则保留这些项。若另换到固定物理
半径而材料尺度在该方向变化，还须保留
$\dot t=-\dot{\log\rho}$；不能混同两种导数。

本篇因此关闭新根的真实解析入口和全频两行局部比较。接下来
必须把这个根接到一侧真实长正段与另一侧完整负分量，支付新的
完整外 Poisson/DN、原两 $\Gamma^*$ 列及扩充后五盒的全网谱
选择。原正帽只给定完整头的高图也不能代替这些端口。新的闭
返回逆、原强标签权以及 nonlinear matching 均未由 (A.1)
单独宣称完成。
