# R331：内部常项与宽矩补偿同时支付新的面积门和旧一层兼容式

日期：2026-11-15。**真实有限 profile 构造，全部推导在纸面完成。** 未执行求积、符号程序、profile 扫描、人工测试或研究计算。

[R328](R328-another-complete-Gaussian-area-excludes-homogeneous-weak-power-packets.md) 排除了不含内部常数项的左右弱幂曲段：新面积 $A_{-1,-3}$ 的第零外矩与旧门一起使原一层严格为正。本稿使用 $A_f=0$ 真正允许的内部常项，并支付它的实际 cutoff 与三矩成本。

关键不是只让一个局部系数变号。内部常项由新面积准确确定，大小为 $O(L)$；它在宽度 $R=\eta L$ 的真实远 cutoff 上接回零。三复矩用三个同尺度的实际 rank-one 包补回。新增四次导数积分是 $O(L^{-1})$，因而 [R325](R325-inward-weak-hook-circles-pay-three-directed-rows-and-the-one-history-compatibility.md) 的严格负兼容方向仍保留。之后使用真实强正方向与同纤维有限频率根，得到同一个实际圆上的联合零。

新结论支付：旧 $A_{-2,-3}$ 的全部三个外矩、新 $A_{-1,-3}$ 的第零外矩、原三条 directed 行及指定完整一层，全部相位。新面积的另外两个外矩与整个第四系统仍未支付。

主要来源：[R308 完整弱核三阶](R308-genuine-derivative-rank-two-circles-with-one-hook-and-complete-third-range.md)、[R317 原 mixed 一层](R317-exact-weak-hook-mixed-correction-and-nonnegative-branch-obstruction.md)、[R320 真实强模块](R320-complete-reflected-area-payment-and-outward-one-history-obstruction.md)、R325、R328，以及 [R293 初选有限观察与真实有限频率根](R293-finite-frequency-zero-of-all-necessary-symmetric-Gaussian-observations.md)。

## 1. 几何与明确的联合目标

固定 R325 同一类真实有限闭 hook 几何
$$
M=0,\qquad T=\kappa_H\mathfrak H,\quad\kappa_H\ne0,
$$
及
$$
h=h_e e^{\varepsilon\sigma^2},\quad
k=\kappa(1-2\varepsilon\sigma^2),\quad
\omega=\kappa/h,\quad
\varepsilon=\kappa^2/4,\quad
0<t:=\kappa^2<1/100.
\tag{1}
$$
$\kappa$ 在整个本稿先固定。下述常数界可以依赖它；不声称在 $\kappa\to0$ 时统一。

沿 R325/R328 的准确规范，
$$
W_*=aR+bS,\qquad Z_*=d_*L+e_*U,\qquad B_{-3}=c_PP,
$$
$$
d_*=\frac{6\kappa^3}{h_e},\qquad
e_*=-\frac{\kappa(15t+1)}{4h_e},
\qquad d_*\ne0,\quad d_*+7e_*\ne0.
$$
对 $u=f\cos\theta+g\sin\theta$、$D=f\odot f-u\odot u$，目标为
$$
I_j\{u,[W_*,P](u;D)\}=0,\qquad j=0,1,2,
\tag{2}
$$
$$
I_0\{u,[Z_*,P](u;D)\}=0,
\tag{3}
$$
$$
F_0=H_2^P=0,\quad
F_1=aH_1^R+bH_1^S=0,\quad
F_2=d_*H_0^L+e_*H_0^U=0,
\tag{4}
$$
及 R325 的准确兼容量
$$
\Psi_\theta=
\frac{N(t)}{24P(t)}
\int\{(f'')^2-(u'')^2\}^2
+\mathcal J_\theta+\frac7{12}C_\theta=0.
\tag{5}
$$
这里
$$
C_\theta=\int(u'')^2\{(f'')^2-(u'')^2\},
\quad
\mathcal J_\theta=\int(u'f''-f'u'')u''f''',
$$
$$
N(t)=16+184t-1713t^2-2475t^3-4590t^4,
$$
$$
P(t)=8+114t-169t^2+231t^3-612t^4.
$$
全部目标对同一个最终圆、全部相位成立。R325 的完整原式表明，(4)、(5)正好使其指定一层
$[\sigma h^{-2}j^0]\mathscr R_{-3,\theta}$ 为零，不遗漏原 local、chain 或 elementary history。

## 2. 一个固定弱核心与非零常项响应

先在一个固定有界局部坐标包络内选实紧 $f_0,g_0$。在 $g_0$ 的严格内部支撑邻域，
$$
f_0(y)=A(b-y)^{5/2},\qquad A\ne0,
$$
而 $g_0$ 在 $f_0$ 的外 cutoff 区为零。选非零 $g_0$ 满足 R325 的一个真实线性条件
$$
\int(f_0'')^2g_0''f_0'''=0.
\tag{6}
$$
可由两个不交内部 bump 的实线性组合完成。此时不急于补三矩，后面将一次补回全部真实目标。

记 $q=f_0''$、$r=g_0''$，并置
$$
W_0=g_0'q-f_0'r,
$$
$$
J_0=\int W_0r q',\qquad
J_{x,0}=\int yW_0q'r',\qquad
j_0=\int W_0q'r'.
$$
直接原幂式给
$$
J_0=-\frac{75A^2}{16}\int(b-y)r^2<0,
$$
$$
M_0:=-\int q q'r^2
=\frac{225A^2}{32}\int r^2>0,\qquad
j_0=\frac23M_0>0.
\tag{7}
$$
此外
$$
K_0=\int q'r'(qg_0-rf_0)=-\frac25J_0,
$$
$$
K_1=-\int q'r'r
=\frac12\int q''r^2
=-\frac{15A}{32}\int(b-y)^{-3/2}r^2\ne0.
\tag{8}
$$
因此把 $f_0$ 在该内部曲段上加真实常数 $c$，将使
$\mathcal K=K_0+cK_1$，却不改 $J_0,J_{x,0},j_0,M_0$。下一节支付这个常数的实际紧支撑恢复；没有在此把它当作无成本 gauge。

## 3. 宽 cutoff 的真实三矩与三个实际补包

取固定实偶 $\chi\in C_c^\infty(\mathbb R)$，满足
$$
\chi=1\ \text{于 }[-1,1],\qquad
\operatorname{supp}\chi\subset[-2,2].
$$
令 $\chi_R(y)=\chi(y/R)$，并取 $R$ 大到使整个固定 $f_0,g_0$ 包络位于 $\chi_R=1$ 内。定义暂未补矩的真实 pair
$$
f_{\rm raw}=f_0+c\chi_R,\qquad g_{\rm raw}=g_0.
\tag{9}
$$
$\chi_R$ 的所有正阶导数与核心正阶 jets 支撑不交，所以原三个复矩没有隐含的交叉项：
$$
\boxed{
\mathbf I(f_{\rm raw}+ig_{\rm raw},
f_{\rm raw}+ig_{\rm raw})
=Q_0+c^2\mathbf I(\chi_R,\chi_R),
}
\tag{10}
$$
其中 $Q_0=\mathbf I(f_0+ig_0,f_0+ig_0)$ 是固定真实复三向量。包括 $I_2$ 中的 $2u'v'$ 在内，交叉项均因正阶导数支撑不交为零。

取一个固定非零实偶紧 bump $\eta$。选三个不同中心 $d_1,d_2,d_3>3$，令
$$
\eta_{j,R}(y)=\eta(y/R-d_j).
$$
先选其母支撑足够小，使三个包互不交，且均在 $\chi_R$ 支撑外。记
$$
m=\int(\eta'')^2>0,\qquad
m_2=\int\{y^2(\eta'')^2+2(\eta')^2\}.
$$
真实矩阵是
$$
\mathbf I(\eta_{j,R},\eta_{j,R})
=
\operatorname{diag}(R^{-3},R^{-2},R^{-1})
\begin{pmatrix}m\\d_jm\\d_j^2m+m_2\end{pmatrix}.
\tag{11}
$$
三列由 $d_j$ 的 Vandermonde 保证可逆。

设 $z_j$ 为复数，并定义实际实 profiles
$$
f_R=f_{\rm raw}+\sum_j\Re(z_j)\eta_{j,R},\qquad
g_R=g_0+\sum_j\Im(z_j)\eta_{j,R}.
$$
解三个准确线性方程求 $z_j^2$，使完整三复矩为零，再任选其复平方根。实际仍是实 $f_R,g_R$；不是复输入控制。由于所有补包与 raw 包络不交，
$$
\boxed{\mathbf I(f_R,f_R)=\mathbf I(g_R,g_R),\qquad
\mathbf I(f_R,g_R)=0.}
\tag{12}
$$
补包内 $f_R,g_R$ 为同一个真实紧函数的两实倍数，所以 $W=0$，$\mathcal K=0$；它们不改(7)、(8)。

从(10)、(11)可直接得固定常数 $C$，使
$$
|z_j^2|\le C(R^3+c^2),\qquad R\ge1.
\tag{13}
$$
这里同时保留 $Q_0$ 的三分量：经尺度对角逆变换后分别是
$R^3Q_{0,0}$、$R^2Q_{0,1}$、$RQ_{0,2}$，以及 $c^2$ 乘固定 $\chi$ 矩向量。

## 4. 真实四次成本界

式(9)中二阶导支撑准确不交，因此其新增四次积分为
$$
c^4R^{-7}\int(\chi'')^4.
$$
由(13)，三个补包的所有四次二阶导积分之绝对值都由
$$
C(R^3+c^2)^2R^{-7}
\le C\{R^{-1}+c^2R^{-4}+c^4R^{-7}\}
\tag{14}
$$
控制。这里的“所有”包括 $\int(f'')^a(g'')^{4-a}$，$a=0,\ldots,4$；不把它们视为独立参数。

(14)也控制这些 rank-one 区域对当前 $m_1(\theta)$ 的全部相位系数。原 R250 公式在一个 rank-one 紧包上分部积分后只留其四次二阶导积分，物理中心不会产生额外增长。核心上的 $m_1$ 只依赖 $f_0'',g_0''$，所以内部常数 $c$ 不改变它。

这一界不声称所有第四观测都是低阶：例如 $\mathcal K$ 的内部常数项正是(8)保留的非零真实通道。这里只控制后面确实使用的 quartic 和面积成本。

## 5. 八副本、镜像与先定的新面积常数

对(12)的整个真实基本圆作八个完整副本：
$$
\alpha_j=(-1)^j\binom7j^{1/3},\qquad
y_j=(j-7/2)D_R,\quad j=0,\ldots,7.
\tag{15}
$$
取 $D_R=D_*R$，其中固定 $D_*$ 足够大，使所有完整包络不交。记
$$
W_8=\sum_{j=0}^7\alpha_j^4>0.
$$
$\alpha_j^4$ 关于中点对称，所以
$$
\sum_j\alpha_j^4y_j=0.
\tag{16}
$$
八副本第三 ruling 的七次差分对任意已固定 $R,c$ 准确为零；同时(16)保留下面实际带位置的一阶历史，不能用无权理想平均替代。

把这一个完整八副本块的弱核心原点放到反射中心 $C_0$ 右侧 $C_0+L$，在左侧放完整镜像。原弱通量、真实反射和(16)给
$$
J=2W_8J_0,\qquad
J_x=2W_8(J_{x,0}+Lj_0),
$$
$$
K(c)=2W_8(K_0+cK_1).
\tag{17}
$$
这些式子包含全部原曲段；宽 cutoff 与 rank-one 补包对此都无贡献。

一旦旧面积第1矩被支付，R317 原身份必给
$$
C_{\rm area}(L)=-2(J+J_x)
=-4W_8(J_0+J_{x,0}+Lj_0).
\tag{18}
$$
它是准确仿射函数，不依赖 $c,R$。R328 的新面积(3)准确为
$$
d_*K(c)-4e_*J-\frac{d_*+7e_*}{3}C_{\rm area}(L).
$$
所以现在先选
$$
\boxed{
c(L)=
\frac{4e_*J+(d_*+7e_*)C_{\rm area}(L)/3
-2d_*W_8K_0}
{2d_*W_8K_1}.
}
\tag{19}
$$
分母非零；$c(L)$ 为真实仿射函数，特别 $c(L)=O(L)$。该选择没有依赖未知的矩补包或以后强幅度：旧面积通过后，实际 $C$ 必须是(18)，而所有那些修正都没有改变(17)。

## 6. 同时让包络合法、成本低阶与朝内负号成立

先取一个固定小数 $\eta>0$，令
$$
R=\eta L.
\tag{20}
$$
raw 包、三个宽补包及八副本的整个支撑均包含在长度为固定常数乘 $R$ 的包络里。取 $\eta$ 足够小，可使右侧整个八副本块严格在 $x>C_0$，左侧镜像严格在 $x<C_0$，并留正间隙。随后只让 $L$ 取足够大的有限值；不在选定 $L$ 后重新缩放已用公式。

沿(19)、(20)，(14)给
$$
R^{-1}+c(L)^2R^{-4}+c(L)^4R^{-7}=O(L^{-1}).
\tag{21}
$$
所有常数可以依赖已经固定的 $\kappa,\eta$。原内部常数虽然是 $O(L)$，其真实接回零的四次导数成本却被准确控制。

条件(6)与 rank-one 补包保证右侧完整块
$$
m_0(\theta)=M\sin^2\theta,\qquad M=W_8M_0>0.
$$
八副本的(16)及真实镜像给
$$
m_0=0,\qquad m_2=2C_0m_1,
$$
$$
m_1=2LM\sin^2\theta+\text{一组一致有界的相位系数}.
\tag{22}
$$
有界性使用(21)，没有把宽包的真实矩或 $x$ 权丢弃。

现在按 R320/R325 进行三次实际强补偿：

1. 用固定强原型的真实复四次根支付总 $\mathcal Q_4$；
2. 用四个 $\mathcal Q_4=0$、正锥为 $\mathbb R^2$ 的强模块，支付全部交叉相位，且不改变所需 $\sin^2\theta$ 主系数；
3. 用 $\mathcal Q_4=\mathcal Z_2=0$ 的实际 isotropic 模块支付剩余 $\sin^2\theta$。

前两步所需目标一致有界。可以用固定线性右逆加一个固定正 balance，令四个真实四次权全正且一致有界；不要求复平方根或四次根随 $L$ 在零点光滑。这里只需要最终一个实际有限选择。

第三步的正四次权满足
$$
w(L)=\frac{16(2LM+O(1))}{3S_*}>0.
$$
每一步在最终位置采用真实完整副本与镜像，保原三矩、完整第三及 $W=K=0$ 的强修正结构。故旧面积(2)全三矩、全相位准确为零。由(18)、(19)，新面积(3)在 $\pi/2$ 也已准确为零，而非仅其 leading 为零。

同一实际圆的兼容量为
$$
\boxed{
\Psi_{\pi/2}(L)
=\frac{2LM}{9}\left(\frac{N(t)}{P(t)}-7\right)+O(1)<0
}
\tag{23}
$$
对足够大有限 $L$ 成立。$O(1)$ 的全部来源已在(14)、(21)、(22)与前两步固定强补偿中控制。准确恒等
$$
7P(t)-N(t)=40+614t+530t^2+4092t^3+306t^4>0
$$
给严格主符号。

这同时支付了新常数的原 cutoff、全部三矩回补和面积目标；不是先把 $\mathcal K$ 当作任意自由常数，再假定其余成本不变。

## 7. 全相位的新面积与十二副本

在弱 hook 和旧面积下，R328 原式为
$$
\mathcal A_Z(\theta)
=d_*\mathcal K_\theta-4e_*\mathcal J_\theta
-\frac{d_*+7e_*}{3}C_\theta.
\tag{24}
$$
令 $q=f''$、$r=u''$。准确有
$$
qu-rf=\sin\theta\,(qg-g''f),\qquad
r'=\cos\theta\,q'+\sin\theta\,g'''.
$$
所以 $\mathcal K_\theta$ 只有
$\sin^2\theta,\cos\theta\sin\theta$ 两系数。这不要求内部常数为零。旧面积已迫 $\mathcal Q_4=0$，故 $C_\theta,\mathcal J_\theta$ 和 $\Psi_\theta$ 也只有这两个系数。

对第6节已经完整三阶的实际圆，作 R325 的十二个真实完整平移副本
$$
(f_j,g_j)=\gamma_jT_{d_j}(f,(-1)^jg),\qquad
\gamma_j^4=\binom{11}{j}.
$$
$\mathcal K,C,\mathcal J,\Psi$ 的系数平移不变；三条 directed 交叉系数至多二次依赖平移。十一差分准确清全部交叉相位。旧面积全三矩零逐副本保持。新面积的 $\pi/2$ 值是零，故(24)现在对全部相位为零。

得到一个固定实际弱宏块 $\mathcal B_-$，满足(2)、(3)、完整三阶，且
$$
\Psi_\theta(\mathcal B_-)=\psi_-\sin^2\theta,\qquad\psi_-<0.
\tag{25}
$$
该块包含真正 $W\ne0$ 区域。它的曲段已是带常项的(9)，因此没有违反 R328 的无常项排除定理。

## 8. 同一 profile 支付 $\Psi$ 与三条完整 directed 行

从构造起点就按 R325/R293 选择原有限
$\mathcal F_\star=(\mathcal F,\int(u'')^4)$ 的实际最大秩母包与纠正方向。取一个在最终不交包络内的 R280/R293 强控制宏块 $\mathcal B_+$，保其五个最后完整 block、实际复制和全部正权。它自己的全部72面积均为零，且
$$
\Psi_\theta(\mathcal B_+)=\psi_+\sin^2\theta,\qquad\psi_+>0.
$$
给它真实四次权 $-\psi_-/\psi_+>0$。不同完整三矩块之间，$PD$ 和 $XD$ 真紧；nested 输出仍可能有二次左尾，但该尾与另一个紧 outer 的 $I_0,I_1,I_2$ 全部准确正交。因此所用两面积、三行与兼容量是实际加法，不删任何微包原尾。

此时(2)、(3)、(5)在整个弱强组合上已全角成立。新面积并没有被冒作一个普通 $C^2$ 约束：带常项弱块已经固定，强宏块的该面积由其原72条件保持为零；我们不对一般 mixed $\mathcal K$ 作未经证明的低阶纤维处理。

仅在强宏块的实际 rank-one 微包内作 R325 第9–10节的两种 even 高频形状。它们始终保持 $\mathcal F_\star$。真实十二个交替位置的正核使三条 directed principal 的非负锥为 $\mathbb R^3$，其矩阵是
$$
\begin{pmatrix}
4&0&0\\
4(a+b)&-4a&0\\
6e_*&2d_*-4e_*&-2d_*
\end{pmatrix},
\qquad \det=32ad_*\ne0.
$$
原全部 copy 权、基线和真实低阶余项都保留。弱块不动，跨完整块项准确为零，故完整三行有一致的
$$
\mathbf F_N(\mathbf z)
=\mathbf F_{\rm base}+\sum_i z_i^2v_i+o_{C^1}(1).
$$
先选有限正 balance 和三列非退化零，再取足够大但有限的一个整数 $N$，得到真实精确根(4)。原十二副本保交叉相位为零，故这是全部 $\theta$ 的零。

$\mathcal F_\star$ 保强宏块的 quartic 值与所有原面积，因此(2)、(3)、(5)在这一有限 $N$ 上继续成立。R325 完整原式遂给
$$
\boxed{
[\sigma h^{-2}j^0]\mathscr R_{-3,\theta}=0
\quad\text{对全部 }\theta.
}
\tag{26}
$$
不是只指定 principal；全部完整基线都进入了有限 $N$ 的实际根。

## 9. 最终位置、原三阶与目标度量

选择顺序不能颠倒：

1. 固定实际有限几何、$\kappa$、初选 $\mathcal F_\star$ 和真最大秩母包／纠正方向；固定 $f_0,g_0,\chi,\eta$ 及三个无量纲补包中心。
2. 固定 $\eta>0$ 和八副本的无量纲间距常数，给出(19)的准确 $c(L)$。
3. 取一个充分大但有限的 $L$，令 $R=\eta L$；完成实际三矩平方根、旧面积强补偿和十二完整副本。所有正幅与支撑此时都是有限真实对象。
4. 固定强控制宏块的全部位置与权重。对这整个有限集合选择共同正物理区间 $I$，使 $h>0$、$x+\omega(s)>0$ 有正间隙；再固定同一个右锚。可先在设计坐标中安排位置，最后在求三行基线以前共同放到合法正半轴。没有在有限频率根之后移动 profiles。
5. 以最终物理位置的真实积分为目标，选固定有限幅盒、足够大有限 $N$ 和精确根。此后不改 $I$、copy 权、锚或几何。
6. 最后共同正幅归一化 $I_0(f,f)=1$，一次固定新 seed 的目标 metric。齐次零式全保持。

原 cutoff 与三个补包为真正紧光滑函数。曲段上 $f'=f_0'$，故 $A_f=0$；cutoff 过渡区 $g=0$，补包和强控制微包上 $W=0$。于是原完整右锚弱 hook 成立。

三矩由(10)–(12)和完整块加法准确支付。每个基本三矩圆的八副本对完整相位第三 ruling 仍逐参数成立；不需要四个形式 cubic period 各自为零。高频仅在整个 hook 平面零的强微包内变化，且共享所有同名实际副本。故第二、第三周期、第三 ruling、两 collar、真实初值及种子均保持。

几何没有改变。最终的 $f$ 一般不同于 R325 原 seed；本稿明确选择一个新的固定目标，而不是声称沿 profile 改动保持旧目标 metric。

## 10. 已付与未付的精确边界

同一个最终真实弱单 hook、导数 rank-two 圆已经支付：

- 原三矩圆及完整三阶；
- $A_{-2,-3}$ 的三个完整外矩、全部相位；
- 新 $A_{-1,-3}$ 的完整第零外矩、全部相位；
- 原三条 directed 行、全部相位；
- 原 local／chain／history 合成的一层(26)、全部相位。

这一结果修复的是 R328 明确发现的新障碍，没有撤销其无常项类的否定。宽恢复与真实矩补偿是本稿新增的支付，不能从内部常项的可调符号省略。

新 $A_{-1,-3}$ 的第1、第2外矩仍欠。全弱强圆的其它 Gaussian 面积、对称乘积和零／一层函数也未由强控制宏块自己的72条件自动支付。canonical 平台、flux、完整第四 period、同一 gauge 的 joint range，以及更高阶与主课题几何标准仍需继续处理。
