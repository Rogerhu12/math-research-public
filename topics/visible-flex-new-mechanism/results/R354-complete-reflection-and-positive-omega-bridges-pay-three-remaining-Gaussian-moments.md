# R354：完整反射、受控 ω 桥与三个剩余 Gaussian 外矩的同时支付

日期：2026-11-15。**完整有限纸面构造；没有执行新的求积、符号程序、profile 扫描、人工检查或科学计算。**

[R351](R351-complete-quadratic-form-and-two-genuine-weak-core-signs-for-the-first-PY-moment.md) 已给真正弱核心的 PY 第一矩两号，但核心尚未补齐三矩与旧面积，不能直接当作完整正纠正。本稿采用另一条完整路线：从 R353 的实际正核得到一个旧门全零的强负块，对整个合法块作反射，得到所缺正号；随后把两者放到一个在设计之初选定的合法物理区间。

负坐标的合法性不由形式算子延拓代替。这里先加强 R37/R70 的真实桥，使整条几何保持任意预定的 \(\omega\) 下界，再在全部有限 profiles 选择以后确定正共振端口高度。最终得到一个**新的实际闭 hook 几何与新 seed**，在同一圆上支付此前13个面积外矩以及完整 \(\mathcal P_1,\mathcal D_0,\mathcal D_2\)，并保持完整三阶、\(\Psi\)、三条 directed 行及指定一层。另给真实十三行双号正锥，以及反射偶圆上的八行正锥。

本稿只要求并重新实现 \(M=0,T=\kappa_H\mathfrak H\ne0\) 和所用 Gaussian 芽。它不宣称这一新几何自动继承另一条既有几何的 universal pure 零、whole \(E\)、Morse 或其他未重新安装的成本条件，也不声称保持此前另一个 seed 的固定度量。这一范围是构造的组成部分。

来源：[R37 原连接](R37-closed-geometry-zero-period-operator.md)、[R70 任意矩桥](R70-zero-matrix-bridges-and-affine-complete-fourth-period.md)、[R89 全场仿射变换](R89-affine-covariance-and-positive-multiple-pair-P1.md)、[R210 真实 hook 与 Klein 闭合](R210-complete-weight-minus4-pure-image-and-finite-pure-closure.md)、[R247 原 hook 平移导子](R247-complete-response-Jacobi-presentation-and-pure-kernel-decomposition.md)、[R259 原尾表](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)、[R308 完整三阶](R308-genuine-derivative-rank-two-circles-with-one-hook-and-complete-third-range.md)、[R325 完整兼容量](R325-inward-weak-hook-circles-pay-three-directed-rows-and-the-one-history-compatibility.md)、[R347 强块完整半平面](R347-exact-coupled-moments-and-cheap-one-sided-positive-negative-Gaussian-correction.md)及 [R353 原正锥](R353-ordered-tails-and-three-positive-centers-pay-the-positive-minus-two-first-moment.md)。

## 1. 原完整目标与两种不同的操作

固定 \(0<\kappa<1/10\)，令 \(t=\kappa^2\)。仍使用原算子
$$
P=\Phi_{r_0},\quad R=\Phi_{r_1},\quad S=\Phi_{s_0},\quad
L=\Phi_{p_0},\quad U=\Phi_{s_1},\quad Y=\Phi_{p_2}.
$$
写
$$
W_*=aR+bS,\qquad Z_*=dL+eU,
$$
$$
a=-\frac{51t^2+2t+8}{64h_e^2},\quad
b=-\frac{34t^2+8t}{64h_e^2},\quad
d=\frac{6\kappa t}{h_e},\quad
e=-\frac{\kappa(15t+1)}{4h_e},\quad
k_*=\frac{db}{2}-ea\ne0.
\tag{1}
$$
沿 R353 记六个 pair 的原外矩为
$$
\mathcal M_j=[W_*,P]_j,\quad
\mathcal A_j=[Z_*,P]_j,\quad
\mathcal B_j=[Z_*,W_*]_j,\quad
\mathcal C_j=[Z_*,Y]_j,\quad
\mathcal P_j=[P,Y]_j,\quad
\mathcal D_j=[W_*,Y]_j.
$$
这里 \([X,Y]_j\) 始终表示
\(I_j(u,[X,Y](u;f^2-u^2))\)，\(u=f\cos\theta+g\sin\theta\)，
且 \(I_2\) 保含 \(2u'w'\)。

本稿把以下两件事严格分开：

1. 在同一个原 profile 代数里，对完整实函数作 \(x\mapsto-x\) 的反射，准确计算所有右尾；
2. 另行选择一条真实几何，使最后整个有限支撑满足 \(x+\omega(s)>0\)。

第二件事不是把一个旧几何的 \(\omega\) 单独增加后仍使用旧 Gaussian 门。下文会实际重造满足指定端芽和低阶算子的闭几何。

## 2. 右锚反射的完整多项式尾

令 \(\mathscr R q(x)=q(-x)\)。所有函数在共同实轴上零延拓；右锚选在全部支撑的右侧，反射前后各自使用同一个真实右零 collar 规则。

原六个二次算子满足
$$
X(\mathscr R f,\mathscr R g)
=\epsilon_X\,\mathscr R X(f,g)+p_{X;f,g}(x),
\qquad \deg p_{X;f,g}\le2,
\tag{2}
$$
其中
$$
\epsilon_P=\epsilon_L=\epsilon_U=\epsilon_Y=-1,\qquad
\epsilon_R=\epsilon_S=1.
\tag{3}
$$
这些符号与原完整伸缩权的奇偶一致，但(2)还必须保留右锚误差。

例如令 \(\mu_j=I_j(f,g)\)，直接换积分变量给
$$
P(\mathscr R f,\mathscr R g)=-\mathscr R P(f,g)+\mu_0,
$$
$$
R(\mathscr R f,\mathscr R g)=\mathscr R R(f,g)+x\mu_0,\qquad
S(\mathscr R f,\mathscr R g)=\mathscr R S(f,g)-\mu_1.
\tag{4}
$$
\(L,U,Y\) 同样由原 local 项与三个右原函数代入得到(2)；差仅为原 E8 左尾表中的二次多项式，系数线性依赖同三个 \(\mu_j\)。等价地，对两边取三次 \(x\) 导数，原完整 local 微分式按(3)相同；再用真实左右 collar 值恢复这一多项式差。没有把非零左尾设为零。

如果内槽 \(D=f^2-u^2\) 的三个矩都为零，则 \(XD\) 在完整包外真紧，(2)中对应的多项式准确为零：
$$
X(\mathscr RD)=\epsilon_X\mathscr R(XD).
\tag{5}
$$
这里 \(\mathscr RD=(\mathscr Rf)^2-(\mathscr Ru)^2\)，不是对普通函数平方差任意改写算子槽。

对任何紧外函数 \(v\) 和真二次多项式 \(p_2\)，
$$
I_j(v,p_2)=0\quad(j=0,1,2).
\tag{6}
$$
特别
$$
I_2(v,Ax^2+Bx+C)
=\int\{2Ax^2v''+2(2Ax+B)v'\}=0.
$$
(6)始终保留两项。

## 3. 全部面积的反射表，适用于完整弱块

由于(5)使两个 inner 输出真紧，外层再用(2)，全部可能的 nested 右锚误差仅是(6)的二次多项式。因此对任意合法三矩圆，不要求导数 rank-one，
$$
\boxed{
[X,Y]_j(\mathscr Rf,\mathscr Rg)
=\epsilon_X\epsilon_Y(-1)^j[X,Y]_j(f,g).
}
\tag{7}
$$
原 \(I_j\) 本身在共同反射下乘 \((-1)^j\)，\(j=2\)的完整配对为偶。

| 完整 pair | \(j=0\) | \(j=1\) | \(j=2\) |
|---|---:|---:|---:|
| \(\mathcal M=[W_*,P]\) | − | + | − |
| \(\mathcal A=[Z_*,P]\) | + | − | + |
| \(\mathcal B=[Z_*,W_*]\) | − | + | − |
| \(\mathcal C=[Z_*,Y]\) | + | − | + |
| \(\mathcal P=[P,Y]\) | + | − | + |
| \(\mathcal D=[W_*,Y]\) | − | + | − |

特别，R353 已付的13个外矩的零集合在反射下保持，而
$$
\boxed{\mathcal P_1(\mathscr Rf,\mathscr Rg)=-\mathcal P_1(f,g).}
\tag{8}
$$
这是整个角函数的身份。不是仅对单个未补矩核心或某个 self 的符号判断。

三矩圆条件本身也保持，因为
\((I_0,I_1,I_2)(\mathscr Rf,\mathscr Rg)
=(I_0,-I_1,I_2)(f,g)\)。
弱通量 \(A_f\mathcal W(f,g)=0\) 保持；
\(A_{\mathscr Rf}=\mathscr RA_f\)，
\(\mathcal W(\mathscr Rf,\mathscr Rg)=-\mathscr R\mathcal W(f,g)\)。
非零 rank-two 区亦保持。

## 4. Ψ 与三个真正 directed 行都是偶的

保 R325 的归一完整兼容量
$$
\Psi_\theta=\frac{N(t)}{24P(t)}D_\theta^{(4)}
+\mathcal J_\theta+\frac7{12}C_\theta,
$$
$$
D_\theta^{(4)}=\int(f''{}^2-u''{}^2)^2,\quad
C_\theta=\int u''{}^2(f''{}^2-u''{}^2),\quad
\mathcal J_\theta=\int(u'f''-f'u'')u''f'''.
\tag{9}
$$
\(D^{(4)},C\) 的密度为偶；\(\mathcal J\)中括号与 \(f'''\)分别变号，故
$$
\boxed{\Psi_\theta(\mathscr Rf,\mathscr Rg)=\Psi_\theta(f,g).}
\tag{10}
$$
本式未先令三个 directed 行为零。

原 directed 配对
$$
H_j^X=-I_j(XD,PD)+2I_j\{u,X(u,PD)\}
$$
由(2)、(5)、(6)给
$$
H_j^X(\mathscr Rf,\mathscr Rg)
=-\epsilon_X(-1)^jH_j^X(f,g).
\tag{11}
$$
所以
$$
F_0=H_2^P,\qquad
F_1=aH_1^R+bH_1^S,\qquad
F_2=dH_0^L+eH_0^U
$$
在反射下分别保持原完整值。第二项的 nested 多项式尾正是由(6)处理，不假设每个中间场紧。

完整三阶不需要把真实几何一并反射。反射后的每个完整宏块仍有原三矩与 hook 条件，其八副本仍是一个基本包及其等间距平移，原七阶有限差分对次数至多六的真实 ruling 多项式继续准确为零。反射只改变相对中心与副本次序；全部三次差分权和仍为零。R308 的完整相位 period 则只用同一 \(T=\kappa_H\mathfrak H\) 和弱 hook。十二副本的 odd 消项同理保留。

## 5. R353 正核给一个完整负 PY 块

这里 \(\mathcal P_1=d_1\sin^2\theta\)不是新增假设：原完整 self
\(S_{P,Y,1}(q)=-\mu_0(q)\mu_2(q)/2\)在合法复 \(q=f+ig\)上为零，故两个 even 系数相等；原十二副本已清 angular odd。所有使用的完整强块及其反射都有这些条件。

R347 的完整有限宽半平面写为
$$
\mathcal F=\frac{\mathcal B_{2,04}}{k_*}-d_1>0,\qquad
\mathcal P_1=d_1\sin^2\theta.
\tag{12}
$$
\(\mathcal B_{2,04}\)沿用该稿的未加倍原规范。
该结论用于实际两坡强块，保母包 self、方差、全部 ordered 尾和完整复制；在固定实际母包邻域后，可先取足够大的有限间距 \(A\)，再取正有限宽度。

从构造起点选择 R353 的24个实际原型时，可以同时要求每列(12)。理由分为两类：

- R353 的前12列采用原两排序、普通／伴随及四变量真 IFT；其零宽极限母包位于 R347 的适用开区间。选 \(A\) 时同时满足正锥所需严格余量与(12)，随后有限正 \(\delta\)恢复全部母参数，严格不等式保持。
- 其余 C0、C1、C2 原型均来自 R346/R348/R349 的同一真实两坡母族；亦可在各自有限参数选择时先要求 R347 的大 \(A\)。随后各组的完整正伸缩保(12)，因为 \(\mathcal B_2/k_*\) 与 \(\mathcal P_1\) 同为权 \(-4\)。

没有在原型冻结以后任意改变其间距。以上均是原有限构造中的初始选择，全部 rank/minor 与严格正核开放性保持。

记 R353 的实际12行矩阵为
$$
M_{12}=(\mathcal B_1,\mathcal B_2,\mathcal D_1,
\mathcal C_0,\mathcal C_1,\mathcal C_2),
$$
各外矩取两个真实 even 系数。它满秩12，并有严格正核 \(k\in\mathbb R^{24}_{>0}\)。
每列另外有
\(\mathcal M_j=\mathcal A_j=\mathcal B_0=0\)。

按真实第四幅 \(k_i\)相加这24个不交完整块，得到 \(\mathcal K_-\)。
原完整三矩块加法使全部13个旧外矩为零。由(12)，
$$
\boxed{
d_1(\mathcal K_-)
=-\sum_i k_i\mathcal F_i<0.
}
\tag{13}
$$
其完整 \(\Psi=\psi_-\sin^2\theta\)，\(\psi_->0\)。
这里的负号来自已付原函数不等式，不来自负第四幅。

取整个反射
$$
\mathcal K_+=\mathscr R\mathcal K_-.
$$
由(7)—(10)，它仍有全部13旧外矩为零，
$$
d_1(\mathcal K_+)=-d_1(\mathcal K_-)>0,\qquad
\Psi(\mathcal K_+)=\Psi(\mathcal K_-)>0.
\tag{14}
$$
\(\mathcal K_+\) 的支撑位于负半轴；它的物理安装将在第8—10节实际支付。

## 6. 一个真实十三行、二十五列的严格正锥

将 R353 的24列各自完整 \(d_1\)值记为行 \(p\)，将(14)作为第25列：
$$
\widehat M_{13}=
\begin{pmatrix}
M_{12}&0\\
p&d_+
\end{pmatrix},\qquad d_+=-pk>0.
\tag{15}
$$
于是
$$
\operatorname{rank}\widehat M_{13}=13,\qquad
\widehat M_{13}(k,1)=0,\qquad(k,1)>0.
\tag{16}
$$
故其真实正锥为全部 \(\mathbb R^{13}\)。这里新增列是一个实际完整反射宏块；它的内部24个块和正幅均已固定，不能把它的各个尾自由拆分。

原24列在正半轴严格不交，新增列在负半轴，因此25个实际列可同时分离。每列的 \(\Psi\) 为严格正系数乘 \(\sin^2\theta\)。本结论不仅给某一个 PY 残差的消去，还给后继联合控制可直接使用的真实满秩正核。

## 7. 同一个最终弱圆支付 PY1，真实 Ψ 成本可任意小

先以 \(h_e=1\) 的归一系数完成 R353 在最后强控制器以前的实际弱基线。原核心、补矩、全部最终正中心固定，
$$
\mathcal M_j=\mathcal A_j=\mathcal B_j=\mathcal C_j=0
\quad(j=0,1,2),\qquad
\mathcal D_1=0,\qquad
\Psi=-\Delta_0\sin^2\theta,\quad\Delta_0>0.
\tag{17}
$$
其完整 \(\mathcal P_1=r\sin^2\theta\) 记录为真实残差，既不假设 \(r\)正，也不删除它。

固定(15)的正核 \(k_{13}>0\)及实右逆 \(R_{13}\)。
把这25个强原型整体作同一个正伸缩 \(S\)，真实第四幅度取 \(S^5c_i(S)\)，其中
$$
c(S)=k_{13}+R_{13}(0,\ldots,0,-r/S).
\tag{18}
$$
原完整权为
$$
\mathcal B_1:-5,\quad\mathcal B_2:-4,\quad
\mathcal D_1,\mathcal C_0:-3,\quad
\mathcal C_1:-2,\quad\mathcal C_2:-1,\quad
\mathcal P_1:-4,\quad\Psi:-7.
\tag{19}
$$
故足够大的有限 \(S\)使 \(c(S)>0\)，且(18)准确给旧12目标增量零和
\(\Delta\mathcal P_1=-r\sin^2\theta\)。
七个逐列恒零的 \(\mathcal M_j,\mathcal A_j,\mathcal B_0\)也保持。

新增兼容量为
$$
\Delta\Psi
=S^{-2}\left(\sum_i c_i(S)\psi_i\right)\sin^2\theta.
\tag{20}
$$
选一个有限 \(S\)使它小于 \(\Delta_0/2\)。
同一个大 \(S\)使新正支撑位于旧弱基线右侧，新负支撑仍在左侧；内部严格间隙保持。没有在求零以后整体平移旧弱块。

最后按 R325/R353 的同一预选 \(F^\star\) 强控制器，先以正幅支付余下 \(\Psi\)，再在其有限观察纤维里取一个有限频率 \(N\)，准确付三个完整 \(F_i\)。控制器自身的全部72面积为零，纤维保持这些值，所以新增 \(\mathcal P_1=0\)也保持。完整低阶与原尾均在同一有限基线中。

至此所有实际 profiles、幅度、宽度、复制、正负位置和有限 \(N\)已经固定，支撑包络有限。尚未因这些代数等式就授其几何合法；下一节支付整个 \(\omega\)下界。

## 8. 带任意严格 ω 下界的真实 frame/scalar 连接

**连接引理。** 给定实数 \(\Omega\)，指定 frame 两端、两端正 \(h\)常值 germ，并有
\(\omega_0,\omega_1>\Omega\)。存在 R37 型真实光滑有限连接，使
$$
h>0,\qquad \omega_s=k_s/(2h),\qquad
F_s=F\Omega_{\rm frame}(k),\qquad
\omega(s)>\Omega
\tag{21}
$$
全程成立，且在固定端数据的小邻域内可光滑选择并保统一正间隙。

证明保留 R37 的先 frame 后 \(h\)顺序。先固定真实平滑 \(k\)路径、全部 frame 修正和端帽，预留一个 \(k_s>0\)小段，再在其后预留 \(k_s<0\)小段。两者的 frame 增量由原满秩词补偿，路径不依赖 \(h\)。

置 \(w_i=\omega_i-\Omega>0\)，取
\(0<\delta<\min(w_0,w_1)/4\)。
可选光滑 \(b_0>0\)，在两个常值端 collar 取指定 \(1/(2h_i)\)，而在全部 \(k_s\ne0\)处足够小，使
$$
\sup_s\left|\int_0^s k_\sigma b_0\,d\sigma\right|<\delta.
\tag{22}
$$
端值过渡放在 \(k_s=0\)的 collar 内，所以不妨碍(22)。

在先正后负的两段取非负紧 \(\chi_\pm\)，令
$$
\frac1{2h}=b_0+\eta_+\chi_++\eta_-\chi_-.
$$
记两次额外累计增量为 \(A>0\)、\(-B<0\)。
所需端值恰是
$$
A-B=w_1-w_0-I_0,\qquad I_0=\int k_sb_0.
\tag{23}
$$
先选一个固定充分大的 \(A\)，则解出的 \(B>0\)。
额外累计项先从0单调升至 \(A\)，再单调降至 \(A-B\)；
其全程下界为 \(\min(0,A-B)\)。
加回(22)，得到
$$
\omega(s)-\Omega
\ge\min(w_0-\delta,w_1-2\delta)>0.
\tag{24}
$$
所有参数有限；小端数据邻域内固定两段、\(\delta,A\)，由(23)光滑选择 \(B\)，正性保持。原 frame 端值没有变化。证毕。

该引理没有对一条旧路径任意重置 \(\omega\)，而是沿同一真实水平微分方程造出整条连接。

## 9. 任意矩桥也可保持这一 ω 下界

R70 的八个完整圆可先做同一个真实 \(\omega\)平移，使全部圆状态满足 \(\omega>\Omega\)并留正间隙。R89 给它们二阶算子的共同可逆仿射作用；因此原 \(B(0)=0\)和八维可逆导数同时保持。没有重新估计一个离散秩。

用第8节连接这些实际圆和指定端点。所有连接在小参数盒中保持统一 \(\omega>\Omega\)，其真实矩成本 \(C(p)\)与辅助圈数 \(K\)无关。R70 同一个方程
$$
K B(p)+C(p)=M_*
\tag{25}
$$
经 \(B(p)+K^{-1}(C(p)-M_*)=0\)的有限维 IFT，给充分大但有限的整数 \(K\)以及准确目标 \(M_*\in\mathfrak{sl}_3\)。整个构造仍在(24)的开区域内。

所以第8节可增强为：**任意指定 frame、正 \(h\)与 \(\omega>\Omega\)两端，任意有限真实八矩目标，均可在同一下界之上准确连接。**

还可保指定的有限非恒端芽。先在两端放真实半芽及光滑常态帽，全部保持 \(\omega>\Omega\)，并保其原 frame 增量、八矩成本与实际端状态；中间仅用(25)补余下的 frame 与矩目标。对下文偶 Gaussian 芽，中心一阶 scalar 速度为零，真倒行与原芽全阶匹配。帽的真实 \(\omega\)由水平式积分；小帽可用原光滑 cutoff并保严格余量，不能独立指定其终值后漏掉积分成本。

这一步只需要保一个有限预定的芽和 M 目标，不依赖未证明的第四成本控制。

## 10. 真实闭 hook、指定 Gaussian 芽和任意下界可同时安排

固定第7节 profiles 的有限区间包络 \(I=[\ell,r]\)，两侧留开 collar。
选
$$
\Omega>\max(0,-\ell)+1.
\tag{26}
$$
取一个固定小正芽宽 \(a_0\)，再选 \(h_e>0\)足够小，使
$$
\frac{\kappa}{h_e e^{\kappa^2a_0^2/4}}>\Omega+1.
\tag{27}
$$
所需 Gaussian 芽
$$
h=h_e e^{\kappa^2\sigma^2/4},\quad
k=\kappa(1-\kappa^2\sigma^2/2),\quad
\omega=\kappa/h
\tag{28}
$$
在 \(|\sigma|\le a_0\)有 \(\omega>\Omega+1\)，且准确满足水平式。

复用 R210 §7/R180 的一个实际 \(M=0,T=t_H\mathfrak H\ne0\)、frame \(I\to I\)环，以及两个实际 \(M=T=0\)、frame \(I\to g_j\)桥。
每条路径有限，故各自可以选一个共同常量平移 \(\omega\mapsto\omega+c\)，令它们全程高于 \(\Omega\)。

这次平移不需要保持每个 profile 值不变；它的算子作用由 R89 全场协变准确给出。关键是原 hook
$$
\mathfrak H=C(P,S)-3C(P,R),\qquad N\mathfrak H=0
\tag{29}
$$
由 R247 已证明，所以纯 \(\omega\)平移保持 \(\mathfrak H\)本身。
零 M、零 T也当然在共同可逆变换下保持。
因此被平移的 hook 环仍有 \(T=t_H\mathfrak H\)，两个 frame 桥仍有 T0。

用第9节在共同新芽(28)与各平移后的常值端口之间造真实 M0、相对 frame \(I\to I\)桥 \(B\)。把目标环或 frame 桥 \(L\)夹成
$$
B\,L\,B^{\rm rev}.
\tag{30}
$$
全部三段 M0，所以完整第三按真实传递相加；原真倒行给
\(T_{B^{\rm rev}}=-T_B\)。于是(30)的第三量准确等于 \(T_L\)。
桥内部的第三 history没有被置零，第四成本也没有被删。
共同芽的偶性使(30)两端采用同一个全阶 Gaussian germ。

现按 R210 §7的同一个 Klein 八边词
\(1,2,1,2,2,1,2,1\)组装：
第一 prototype 用此 hook 环接第一个 frame 桥，第二 prototype 用第二个 frame 桥。
每种真实 prototype 位移在四个 ambient 左旋位置各出现一次，
\(\sum_{g\in\{I,g_1,g_2,g_1g_2\}}g=0\)，故中心线位移准确相消。
frame、scalar 和完整 germs亦闭合，且
$$
M=0,\qquad T=4t_H\mathfrak H\ne0,\qquad
\omega(s)>\Omega.
\tag{31}
$$
所有拼接长度、整数、帽、位移和历史均有限真实。
由(26)，整个 profile 包络有
$$
\boxed{x+\omega(s)>\ell+\Omega>1.}
\tag{32}
$$
这支付负支撑与正支撑同时合法；没有穿越移动极点，也没有把 universal 延拓冒作物理浸入。

原 \(\alpha_s=h^2T\)、\(X=\alpha+uN\)、\(u=h/(x+\omega)>0\)因此给真实正则闭浸入带。Klein 闭合不证明这个带嵌入，亦不证明任何 reach。

## 11. 为什么可在 profiles 以后选 he，且不改变已付等式

对固定 \(\kappa\)，(1)中 \(W_*\)只乘 \(h_e^{-2}\)，\(Z_*\)只乘 \(h_e^{-1}\)。因而各完整目标相对于 \(h_e=1\)为：

| 目标 | 共同乘数 |
|---|---:|
| \(\mathcal M_j,\mathcal D_j,F_1\) | \(h_e^{-2}\) |
| \(\mathcal A_j,\mathcal C_j,F_2\) | \(h_e^{-1}\) |
| \(\mathcal B_j\) | \(h_e^{-3}\) |
| \(\mathcal P_j,F_0,\Psi\) | \(1\) |

所有母包方程和有限纤维使用原实际 profile 泛函；这里仅将原几何常数代入(1)，没有对已求根的 profiles 再作空间平移。完整零等式因此都保持；\(k_*\)也乘 \(h_e^{-3}\)，所以(12)不变。

\(\Psi\)使用(9)的原归一值，其系数只依赖 \(t\)。原指定一层是 R325 的
$$
c_P(A_0F_0+A_1F_1+A_2F_2)+B_\kappa\Psi;
$$
故三 F 与 \(\Psi\)全零后，该层在新 \(h_e\)下仍准确为零。

完整第二／第三 range由新几何(31)、三矩、弱 hook及原八副本 polynomial ruling身份重新得到；不需同旧几何比较 canonical 高阶成本。
最终 seed 度量
\((X+\epsilon Y_f)^*\mathrm e\)
在所有有限选择以后一次固定，随后与圆参数 \(\theta\)无关。

## 12. 更直接的整体弱圆配对一次支付三个新矩

第3—4节已经对任意完整合法弱圆证明反射公式；并不限于第5节的强纠正器。因此有一条更短的最终构造。

取 R353 **全部位于正半轴**的最终完整弱圆 \((f_+,g_+)\)，其中旧13矩、\(\Psi\)和三条 \(F_i\)都已为零。它的所有真实有限 choices仍按 \(h_e=1\)归一选择。定义
$$
f_{\rm ev}=f_++\mathscr Rf_+,\qquad
g_{\rm ev}=g_++\mathscr Rg_+.
\tag{33}
$$
两完整支撑在正、负半轴严格分离，因此 \(f_{\rm ev},g_{\rm ev}\)是真实紧 \(C^\infty\)偶函数；原弱 rank-two 开段与其反射均保留。

每一半的 \(D_\theta\)单独三矩为零。原 R325 完整块加法于是适用：两个 inner E8输出各自真紧；nested输出可能留下的真二次尾与另一半紧 outer的三个矩由(6)准确正交。故所有 Gaussian面积、三个 directed行按两半准确相加，\(\Psi\)的原 local密度亦相加。
没有把一半内部未闭合的微包各自当成无尾输入。

R353 的13个旧零在每一半仍分别为零；(7)又准确给
$$
\mathcal P_1(f_{\rm ev},g_{\rm ev})=0,\qquad
\mathcal D_0(f_{\rm ev},g_{\rm ev})=0,\qquad
\mathcal D_2(f_{\rm ev},g_{\rm ev})=0.
\tag{34}
$$
不需要先知道这三条在正半圆上的残差或符号。
由(10)—(11)，\(\Psi\)与三 F都是两个原零相加，仍为零。
完整第三按第4节重新支付，弱hook不因不交相加改变。

现在将(33)的全部有限包络代入第10节，实际构造(31)的闭几何。第11节使所有零等式在实际所选 \(h_e\)下保持，(32)给两半同一物理域。这不是在一个含负模块的旧完成圆上再反射并假定支撑无交；反射的起点明确是 R353 的全正圆。

若后续需要严格负 \(\Psi\)储备，可改取 R353 最后控制器以前的全正基线再用(33)。旧13矩同样零，三条新矩由(34)付清，且 \(\Psi=-2\Delta_0\sin^2\theta<0\)。最后可把原 \(F^\star\)强控制器及其反射成对加入，并同步做其有限纤维变化；全部72面积零保持，\(\Psi\)及三F的真实控制列只共同乘2，原有限频率正核证明不变。故这个入口同样给最终偶圆，并保供后继使用的实际选择顺序。

## 13. 反射偶圆上的真实八行正锥

对 R353 的24个全正强原型，分别取它与其完整反射的等幅和。各正支撑原本严格分离，负支撑是其反射，故这24个新完整列也能同时分离。

由(7)，以下所有目标在每个新列上自动为零：
$$
\mathcal M_j,\mathcal A_j\ (j=0,1,2),\quad
\mathcal B_0,\mathcal B_2,\mathcal C_1,\quad
\mathcal P_1,\mathcal D_0,\mathcal D_2.
\tag{35}
$$
其中 \(\mathcal M_j,\mathcal A_j,\mathcal B_0\)在原列已为零；其余由空间反射奇性清去。不是把全部旧目标都称为对称自动零。

剩余有待联合控制的旧目标是
$$
(\mathcal B_1,\mathcal D_1,\mathcal C_0,\mathcal C_2),
$$
各两个 even 系数，共八行。记从 R353 的 \(M_{12}\)删除 \(\mathcal B_2,\mathcal C_1\)四行的投影为 \(\Pi_8\)，则完整真实矩阵恰为
$$
\boxed{M_8=2\Pi_8M_{12}.}
\tag{36}
$$
原12行独立，所以这八行独立；原严格正 kernel仍在其核内。
因此
$$
\operatorname{rank}M_8=8,\qquad
\operatorname{cone}_+(M_8)=\mathbb R^8.
\tag{37}
$$
每列仍有严格正 \(\Psi\)，完整伸缩权分别为 \(-5,-3,-3,-1\)。
\(\mathcal P_0,\mathcal P_2\)在这些列上的真实值保留，当前不设为零。
第13节给后继继续这两个偶目标的实际旧门控制库；不使用第6节的十三行 cone去假称已付一个未在矩阵中的目标。

## 14. 准确结论与后继范围

存在一条第10节的真实闭正则 hook 几何，具有原小共振 Gaussian芽；同一个实紧 \(C^\infty\)偶弱圆有非零导数 rank-two区，并准确满足
$$
\boxed{
\mathcal M_j=\mathcal A_j=\mathcal B_j=\mathcal C_j=\mathcal D_j=0
\quad(j=0,1,2),\qquad
\mathcal P_1=0
}
\tag{38}
$$
对全部相位成立。同一个圆还保三矩、完整三阶、
\(\Psi=F_0=F_1=F_2=0\)及原指定一层。

已经支付的是16个面积外矩；只剩 \(\mathcal P_0,\mathcal P_2\)。
形式 even位置数不是独立秩。第6节的13行正锥和第13节的8行正锥分别是已明确实现的联合接口，不等于全72面积或完整第四已经完成。

本稿不授一个任意冻结旧几何或旧窄区间中的反射纠正；(27)—(31)属于新设计。
特别，另一条几何上的 universal pure、whole self、全部period、同一gauge、Morse或其他已付几何观察，不能仅凭(31)移植。
后继若需把它们与本稿的负支撑联合，应在同一 \(\omega>\Omega\)区域内支付相应完整成本和正则约束。

完整第四、更高阶收敛、同一固定度量的有限连续嵌入族、闭面与全时全域reach/宏观幅度仍须继续。这里完成的是三个原未付外矩、两个实际正锥及其真实物理域；没有用未补矩弱核心、无穷尺度或假紧primitive代替答案。
