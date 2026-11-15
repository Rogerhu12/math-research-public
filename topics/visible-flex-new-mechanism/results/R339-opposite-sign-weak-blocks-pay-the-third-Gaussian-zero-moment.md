# R339：异号 C 的真实弱块同时支付第三面积第零矩与全部既付门

日期：2026-11-15。**真实有限构造，全部在纸面完成。** 未执行求积、符号程序、profile 扫描、人工测试或研究计算。

[R337](R337-true-translation-excludes-the-same-sign-reflected-weak-block-architecture.md) 排除了正物理区间内仅含 $C<0$ 反射弱块的架构。本稿真正加入一个 $C>0$ 的新弱块。它的内部幂曲段朝向与原负块相反，内部常项、远宽 cutoff、三矩补偿和旧面积修正全部实际支付。

新块放在一个足够右但有限的真实位置，正四次幅度由原面积的中心公式准确决定。其对 $\Psi$ 的成本随该实际中心的倒数趋小。因此可以清掉 R337 的新面积，仍保留负 $\Psi$ 储备；然后用 R334 的四个真实强面积方向及最后同纤维有限频率根，保住此前已付的所有门。

最终是同一个真实圆上的联合结论：两完整 Gaussian 面积、第三面积的第零外矩、$\Psi$、三条完整 directed 行和指定完整一层，全相位同零。仍不声称完整第四或 joint 已解。

主要来源：[R320 真实强正锥](R320-complete-reflected-area-payment-and-outward-one-history-obstruction.md)、[R331 内部常项及宽矩补偿](R331-interior-constant-and-wide-moment-repair-pay-the-new-area-and-old-layer.md)、[R332 原平移与第1矩](R332-true-translation-and-reflection-pay-the-next-Gaussian-area-moment.md)、[R334 完整第2矩支付](R334-positive-dilations-pay-the-full-second-Gaussian-area-with-the-old-layer.md)、R337，以及 [R325 完整三行](R325-inward-weak-hook-circles-pay-three-directed-rows-and-the-one-history-compatibility.md)、[R293 有限观察与有限频率根](R293-finite-frequency-zero-of-all-necessary-symmetric-Gaussian-observations.md)。

## 1. 同一几何与联合目标

固定 R331/R334 的同一实际有限几何
$$
M=0,\qquad T=\kappa_H\mathfrak H,\qquad \kappa_H\ne0,
$$
及其小共振 Gaussian 端芽
$$
h=h_e e^{\varepsilon\sigma^2},\quad
k=\kappa(1-2\varepsilon\sigma^2),\quad
\omega=\kappa/h,\quad
\varepsilon=\kappa^2/4,\qquad 0<t:=\kappa^2<1/100.
\tag{1}
$$
沿用原算子及系数
$$
P=\Phi_{r_0},\ R=\Phi_{r_1},\ S=\Phi_{s_0},\
L=\Phi_{p_0},\ U=\Phi_{s_1},
$$
$$
W_*=aR+bS,\qquad Z_*=d_*L+e_*U,
$$
$$
a=-\frac{51t^2+2t+8}{64h_e^2},\quad
b=-\frac{34t^2+8t}{64h_e^2},\quad
d_*=\frac{6\kappa t}{h_e},\quad
e_*=-\frac{\kappa(15t+1)}{4h_e}.
$$

令
$$
u=f\cos\theta+g\sin\theta,\qquad
D=f\odot f-u\odot u,
$$
并定义
$$
\mathcal M_j=I_j\{u,[W_*,P](u;D)\},\qquad
\mathcal A_j=I_j\{u,[Z_*,P](u;D)\},
$$
$$
\mathcal B_0=I_0\{u,[Z_*,W_*](u;D)\}.
\tag{2}
$$
非零 Gaussian 公共因子不改变这些零条件。

最终要同时得到
$$
\boxed{
\mathcal M_j=\mathcal A_j=0\ (j=0,1,2),\qquad
\mathcal B_0=0,\qquad
\Psi=F_0=F_1=F_2=0
}
\tag{3}
$$
对全部 $\theta$ 成立。$\Psi,F_i$ 使用 R325/R334 的完整规范，不改成 principal 近似。

保留
$$
C_\theta=\int(u'')^2\{(f'')^2-(u'')^2\},\qquad
J_\theta=\int(u'f''-f'u'')u''f''',
$$
$$
\Psi_\theta=\frac{N(t)}{24P_0(t)}
\int\{(f'')^2-(u'')^2\}^2+J_\theta+\frac7{12}C_\theta.
\tag{4}
$$
$N,P_0$ 是 R334 的原正多项式。真正的新方向是 $C_\theta$ 的符号，而非重命名旧负分支的位置。

## 2. 一个固定负块及真实中心公式

按 R331 §§2–7 和 R332，先取一个真实负宏块 $\mathcal B_-$，尚未加最后强控制器。它已经支付：

- 原三矩、弱单 hook 与完整三阶；
- 旧面积 $\mathcal M_0,\mathcal M_1,\mathcal M_2$；
- 新面积 $\mathcal A_0,\mathcal A_1$。

其十二复制清 odd 相位后，有
$$
C_\theta(\mathcal B_-)=C_-\sin^2\theta,\qquad C_-<0,
$$
$$
\Psi_\theta(\mathcal B_-)=-\Delta\sin^2\theta,\qquad\Delta>0.
\tag{5}
$$
$C_-<0$ 与原负储备都在同一充分大有限内部距离分支上选择。

设其各完整反射基块的正四次权为 $\rho_j$，实际反射中心为 $X_{-,j}$。以这些实际权定义
$$
\overline X_-=
\frac{\sum_j\rho_jX_{-,j}}{\sum_j\rho_j}.
$$
可用原等差十二副本关于一个共同宏块中心对称放置，所以这恰是预先选定的真实宏块中心；各 $X_{-,j}$ 仍不同。把整个有限包络放在一个允许的正区间中，保证所有 $X_{-,j}>0$，从而 $\overline X_->0$。

R337 的完整原尾与平移公式给
$$
\boxed{
\mathcal B_0(\mathcal B_-)
=\frac23\chi_\kappa C_-\overline X_-\sin^2\theta,
}
\tag{6}
$$
其中
$$
\chi_\kappa=\frac{\kappa(28t^2-35t-4)}{64h_e^3}\ne0.
\tag{7}
$$
本稿将用另一个真实弱块抵消(6)，不修改(5)的核心或其宽过渡。

## 3. 反向核心产生不同的 C，而非只移动原分支

取 R331 使用的固定核心 $f_0,g_0$。在 $g_0$ 的支撑邻域，
$$
f_0(y)=A(b-y)^{5/2},
$$
且
$$
\int(f_0'')^2g_0''f_0'''=0.
$$
记其真实常数为
$$
J_0<0,\qquad j_0=\int W_0f_0'''g_0'''>0,\qquad
J_{x,0}=\int yW_0f_0'''g_0''',
$$
$$
K_0=-2J_0/5,\qquad
K_1=\frac12\int f_0''''(g_0'')^2\ne0,
$$
其中 $W_0=g_0'f_0''-f_0'g_0''$。

现在取真正反向的核心
$$
f_0^+(y)=f_0(-y),\qquad g_0^+(y)=g_0(-y).
\tag{8}
$$
它在活动区是 $A(b+y)^{5/2}$，并非原核心的平移。原线性弱条件仍为零。换元准确给
$$
J_0^+=J_0,\quad J_{x,0}^+=J_{x,0},\quad
j_0^+=-j_0,\quad K_0^+=K_0,\quad K_1^+=K_1.
\tag{9}
$$
例如反射同时翻转 $W_0,f_0''',g_0'''$，所以无 $y$ 的三因子 $j_0$ 翻号，而带 $y$ 的 $J_{x,0}$ 不变。$K_1$ 的非零性也保留。

在该核心加入真实内部常数 $c$；其作用仍准确为
$$
K=K_0+cK_1,
$$
而 $J_0,J_{x,0},j_0$ 不变。下一节支付其原 cutoff 与矩成本。

## 4. 真实宽恢复与三个补包，原成本不省略

按 R331 取固定偶 cutoff $\chi$，$\chi=1$ 于核心包络，令
$$
f_{\rm raw}^+=f_0^++c\chi_R,\qquad
g_{\rm raw}^+=g_0^+,\qquad \chi_R(y)=\chi(y/R).
$$
所有正阶 cutoff jets 与核心支撑不交。原三复矩准确为
$$
Q_0^++c^2\operatorname{diag}(R^{-3},R^{-2},R^{-1})\mu_\chi.
\tag{10}
$$

在 cutoff 外选三个真实宽 rank-one 包，宽度同为 $R$、无量纲中心互异。其三矩矩阵是
$$
\operatorname{diag}(R^{-3},R^{-2},R^{-1})
\begin{pmatrix}
m&m&m\\
d_1m&d_2m&d_3m\\
d_1^2m+m_2&d_2^2m+m_2&d_3^2m+m_2
\end{pmatrix}.
\tag{11}
$$
它由真实 Vandermonde 可逆。解原三线性式求复幅平方 $z_j^2$，再取其复平方根的实、虚部作为两条真实实 profiles 的系数。这样准确恢复
$$
\mathbf I(f,f)=\mathbf I(g,g),\qquad \mathbf I(f,g)=0.
\tag{12}
$$
所有补包上 $W=K=0$；它们不改变(9)。

同一个真实矩阵给
$$
|z_j^2|\le C(R^3+c^2),
$$
而全部新增四次二阶导积分由
$$
C\{R^{-1}+c^2R^{-4}+c^4R^{-7}\}
\tag{13}
$$
控制。这个界包括原 cutoff 与三个补包，不把内部常数当作无成本控制。后面所用 $\Psi_+$ 更直接采用最终完整积分的实际值，因而也没有以(13)替代其成本。

## 5. 原面积正锥使反向基块真实达到 C>0

对第4节的基本三矩圆作原八完整复制，权为
$\alpha_j=(-1)^j\binom7j^{1/3}$，相对位置关于中点对称。记
$W_8=\sum\alpha_j^4>0$。
把完整右块的核心原点放在中心右侧距离 $L_+$ 处，左侧放它的真实 profile 镜像。

由(9)及真实四次权的零一阶均值，
$$
J=2W_8J_0,\qquad
J_x=2W_8(J_{x,0}-L_+j_0),
$$
$$
K(c)=2W_8(K_0+cK_1).
\tag{14}
$$
一旦旧面积付清，原弱身份必给
$$
\boxed{
C_{\rm tar}^+(L_+)
=-2(J+J_x)
=-4W_8(J_0+J_{x,0}-L_+j_0)>0
}
\tag{15}
$$
对充分大有限 $L_+$ 成立。这里的正号来自(8)的真实朝向改变。

新 $\mathcal A_0$ 在 $\pi/2$ 的完整式是
$$
d_*K(c)-4e_*J-\frac{d_*+7e_*}{3}C.
$$
因此先取准确的
$$
\boxed{
c_+(L_+)=
\frac{4e_*J+(d_*+7e_*)C_{\rm tar}^+(L_+)/3
-2d_*W_8K_0}
{2d_*W_8K_1}.
}
\tag{16}
$$
分母非零，且 $c_+(L_+)=O(L_+)$。再取 $R=\eta L_+$，固定 $\eta>0$ 足够小，使完整宽恢复、八副本与镜像严格不交并留有间隙。式(13)此时为 $O(L_+^{-1})$，所有对象仍是有限正宽。

现在支付旧面积，不能沿用只适合一个符号的 isotropic 修正。先用 R320 的真实强原型及一个固定复四次根支付 $\mathcal Q_4$；这仅是在整个 hook 平面零的实强 pair 上作正交变换与正幅度。随后使用 R320 §5 的四个 $\mathcal Q_4=0$ 强模块。其两个 $m_1$ 系数向量的正锥为 $\mathbb R^2$，并有严格正 balance。

反向核心留下的 $m_1$ 可能为负，也可能另有交叉相位；这是一个实际有限二维目标。上述正锥直接用四个有限正四次权准确支付它。每个强模块与其镜像一同放置，保持全局中心偶性。旧 $m_0=0$ 和中心反射的真实关系 $m_2=2X_0m_1$ 随之给出全部旧三面积。

所有新强区都满足 $W=K=0$，所以没有改变(14)。旧面积通过以后，实际 $C$ 必须等于(15)。因此(16)真的使 $\mathcal A_0(\pi/2)=0$；没有形成一个以未知强补偿成本为自由变量的循环方程。

整个步骤保真实三矩与完整第三。相位变换只用于强 hook 原型，选择的是新的真实 $f,g$；没有把固定旧几何成本的任意输入 phase 当作许可。

## 6. 十二副本给完整正 C 宏块

第5节的基块仍为中心偶 pair。原弱恒等与 $\mathcal Q_4=0$ 使 $C_\theta,\Psi_\theta$ 只有
$\sin^2\theta,\cos\theta\sin\theta$ 两项；新 $\mathcal A_0$ 的 $\pi/2$ 值已经为零。

按原十二完整副本，以 $\rho_j=\binom{11}{j}$ 和 $g$ 翻号 $(-1)^j$ 清 odd 项。R332 的真实算子平移同时给
$$
\mathcal A_0=\mathcal A_1=0
\quad\text{全部 }\theta.
\tag{17}
$$
旧面积全三矩及完整三阶逐副本保持。得到一个真实宏块 $\mathcal B_+$，使
$$
C_\theta(\mathcal B_+)=C_+\sin^2\theta,\qquad C_+>0,
$$
$$
\Psi_\theta(\mathcal B_+)=\psi_+\sin^2\theta,
\tag{18}
$$
其中 $\psi_+$ 是该实际完整 profile 的有限实数。

还可选择 $L_+$ 足够大，使 $\psi_+>0$。因为在复制前
$$
\Psi_{\pi/2}
=\frac{N(t)}{24P_0(t)}D_4+2W_8J_0+\frac7{12}C_{\rm tar}^+(L_+),
$$
$D_4\ge0$，$J_0$ 固定，而最后一项趋正无穷。十二正四次权只乘共同正数。因此下文可固定
$$
\psi_+>0.
\tag{19}
$$
这不需要忽略补包或强修正；所有那些贡献都已包含在完整非负 $D_4$ 中。

新 $\mathcal A_2$ 一般尚有两个真实 even 系数。我们不在这里把它们置零，后面以 R334 的实际两维正锥一起支付。

## 7. 真实中心与正权准确消去 R337 的面积

先固定两个宏块的全部内部形状、宽度、补包、复制数与内部相对间距。负块的最终真实中心 $\overline X_->0$ 已固定，且整个包络位于合法正半轴。

正块的十二中心取
$$
X_{+,j}=\overline X_++(j-11/2)D_+,
$$
其中 $D_+>0$ 已固定为足够大的实际复制间距。由于 $\rho_j=\rho_{11-j}$，
$$
\sum_j\rho_jX_{+,j}
=\left(\sum_j\rho_j\right)\overline X_+.
\tag{20}
$$
它们并非同一个中心。把 $\overline X_+$ 取足够大且有限，可使全部正块支撑位于负块右方、互不相交、且每个实际中心为正。

R337 的完整公式现在同时适用于两种符号：
$$
\mathcal B_0(\mathcal B_\pm)
=\frac23\chi_\kappa C_\pm\overline X_\pm\sin^2\theta.
\tag{21}
$$
其中所有原交叉相位与逐副本 $A_0=b_0\cos\theta\sin\theta$ 项，均由原十一差分连同实际一次中心准确消去。

给正块取真实正四次权
$$
\boxed{
w_+=-\frac{C_-\overline X_-}{C_+\overline X_+}>0.
}
\tag{22}
$$
其实际 profile 幅度是 $w_+^{1/4}$。于是
$$
\boxed{
\mathcal B_0(\mathcal B_-+w_+^{1/4}\mathcal B_+)=0
\quad\text{全部 }\theta.
}
\tag{23}
$$
这不是 signed 成本的形式相消；两条 profile 都是真实有限对象，系数为正四次幅。

$\Psi$ 的完整局部积分平移不变。正块的全部 $\psi_+,C_+$ 已在移动以前固定。因此
$$
w_+\psi_+
=\frac{-C_-\overline X_-\psi_+}{C_+\overline X_+}
\longrightarrow0
\qquad(\overline X_+\to+\infty).
\tag{24}
$$
取一个足够右但有限的 $\overline X_+$，使
$$
w_+\psi_+<\Delta/2.
$$
此时两个真实弱宏块合起来仍满足
$$
\Psi_\theta=-\Delta_1\sin^2\theta,\qquad
\Delta_1=\Delta-w_+\psi_+>\Delta/2.
\tag{25}
$$
两完整块的 $\mathcal M_j,\mathcal A_0,\mathcal A_1$ 继续为零。两个弱块原所有 tail、矩补偿和第四成本都进入了(22)、(24)的实际数值定义；没有把 $\psi_+$ 替换为 principal。

必须注意：(22)使用最终物理中心。此后不能再把整个组合共同平移而声称(23)不变。新的面积所保留的正是原坐标中的中心项。

## 8. 支付新 A2 时明确保留第三面积第零矩

两个弱宏块的实际剩余 $\mathcal A_2$ 是一个有限二维 even 向量。它的全部 odd 项已经清去；$\mathcal A_0,\mathcal A_1$ 为零，所以 R332 的真实平移式使其各自第2矩不随最终搬移改变。

使用 R334 §§3–8 的四个实际强面积模块：

- 两个不同 $\alpha$ 给不同的方向 $(\alpha\beta,1)$；
- 原 R267 正宽母根两边的真实参数给每条方向的正、负输出；
- 四个正四次权准确支付当前实际 $\mathcal A_2$ 两向量；
- 共同正伸缩 $\Lambda$ 及四次权 $\Lambda^5$ 保目标，而新增完整 $\Psi$ 恰为 $\Lambda^{-2}S_\Psi$。

取有限 $\Lambda$ 足够大，使
$$
\Lambda^{-2}S_\Psi<\Delta_1/2.
\tag{26}
$$
把这些有限模块放到预先保留的不交正包络中；原 $\mathcal A_0,\mathcal A_1$ 及旧三面积使其第2矩对这种最终搬移准确不变。

这里必须额外使用 R337 §7 已证明的新事实：
$$
\boxed{\mathcal B_0=0\quad
\text{在 R334 的每个强面积模块上，全相位成立}.}
\tag{27}
$$
它不是所有强 profile 的通则。证明使用本模块的两组奇数次 TM 反序、偶母包、原 $C_\theta=0$、新 $\mathcal A_0=0$、真实算子平移，以及十二副本的 odd 消去。其二次原尾已被准确保留。

因此四个强模块不会重新打开(23)。得到一个固定实际组合 $\mathcal B_{\rm pre}$，满足
$$
\mathcal M_j=\mathcal A_j=0\quad(j=0,1,2),\qquad
\mathcal B_0=0,
$$
$$
\Psi_\theta(\mathcal B_{\rm pre})
=-\Delta_2\sin^2\theta,\qquad
\Delta_2>\Delta_1/2>0.
\tag{28}
$$
上述支付没有改变两个弱核心、它们的物理中心或(22)的权。

## 9. 最后同纤维有限频率根不破任何新面积

从构造起点按 R325/R293 初选强控制器所用的实际有限
$$
\mathcal F_\star=(\mathcal F,\int(v'')^4),
$$
并选其真正最大秩母包、固定非零 minor、纠正方向和两种 even 振荡形状。四个面积模块以及两个弱块不需要被假定为这个 regular 母包，也不参与最后形状纠正。

在最终不交正位置构造一个 R280/R293 的完整强控制宏块 $\mathcal C$。其所有实际副本和五个最后 block 的正权都先固定，自己的全部72 Gaussian 面积准确为零。特别当前三个面积中所列的七个外矩均为零。它还有
$$
\Psi_\theta(\mathcal C)=\psi_{\mathcal C}\sin^2\theta,\qquad
\psi_{\mathcal C}>0.
$$
给它正四次权 $\Delta_2/\psi_{\mathcal C}$，准确支付(28)的负值。

此后只在 $\mathcal C$ 的强 rank-one 微包内作原同 $\mathcal F_\star$ 的有限频率变化。R325 的两种真实 even 形状、实际交替位置及完整 copy 权给三行的正锥 $\mathbb R^3$。最终基线包含本稿两个弱块、四个强面积块、控制器的全部原值和真实最终位置：
$$
\mathbf F_N(\mathbf z)
=\mathbf F_{\rm base}+\sum_i z_i^2v_i+o_{C^1}(1).
\tag{29}
$$
$\mathbf F_{\rm base}$ 是实际任意有限三向量，未被只取最高平方代替。

取严格正 balance 与三个独立列，固定其余正幅。非退化零在小 $C^1$ 扰动下稳定，故一个足够大的有限整数 $N$ 给完整精确根
$$
F_0=F_1=F_2=0.
\tag{30}
$$
原十二副本及完整相位归约使(30)对所有 $\theta$ 成立。

同一个 $\mathcal F_\star$ 纠正保持控制器的全部72面积，故它对新 $\mathcal B_0$ 仍准确贡献零；其 quartic 值也保持，所以 $\Psi=0$ 不变。两个弱块、(22)的实际中心平衡、四个 $I_2$ 支付模块全部固定。于是(3)在同一个有限 $N$ 上真实成立。

R325 的完整一层恒等最终给
$$
\boxed{
[\sigma h^{-2}j^0]\mathscr R_{-3,\theta}=0
\quad\text{全部 }\theta.
}
\tag{31}
$$
它保完整 local、chain、elementary history 和初始基线，不仅是 principal 为零。

## 10. 完整块加法、原第三与真正的选择顺序

所有加入对象都单独满足完整三矩圆。因而其每个 $D_\theta$ 的二次算子 $XD_\theta$ 真紧。不同完整块之间的同点 inner 乘积为零；同块 nested 输出虽可能带二次左尾，其与另一个紧 outer 的原 $I_0,I_1,I_2$ 全部正交。特别第三面积的两 directed 方向都按原式相加。

$\Psi$ 是完整 local 四次积分，因此也准确相加。上述理由适用于完整三矩块，不是把单个非三矩闭的微包尾删除。

真正的顺序为：

1. 固定有限几何与非零 $\kappa$；从起点选控制器的 $\mathcal F_\star$、最大秩母包和纠正方向。
2. 依 R331 完成一个有限负块的全部内部宽恢复、矩补偿、旧面积修正与复制，并把它放到一个固定合法正位置 $\overline X_-$。
3. 按 §§3–6 完成不同朝向的正 $C$ 块。先固定其有限 $L_+$、内部常数、真实宽补包、全部原面积修正和相对复制位置，得到实际 $C_+,\psi_+$。
4. 选择足够右但有限的最终 $\overline X_+$，然后且仅然后取(22)的正权；此时(23)及负储备都准确成立。
5. 读取两个固定弱块的完整 $\mathcal A_2$，使用 R334 四个实际强模块支付。正伸缩及最终正位置都按(26)、(27)固定；不移动已有两个弱宏块。
6. 在其余最终不交包络内构造强控制器，固定其所有正权，确定(29)的实际基线及拟求的有限频率方程；此时尚未选取最后的有限 $N$。
7. 取共同有限正 $I$，其左侧留合法间隙，右端在上述全部有限支撑右方；同一右锚也在全部支撑右方。可以从开始就用固定几何允许的正半轴作位置设计，最后只选包含全部既定坐标的有限区间，不能再整体平移以“放入”该区间。
8. 完成一个有限 $N$ 后，作一次共同正幅归一化，固定最终 seed 的目标 metric。所有齐次零式和中心平衡都保持。

固定有限几何满足 $h>0$、$\omega$ 有界，所以原合法性条件 $x+\omega(s)>0$ 在一个充分右的半轴上留有正间隙。所有物理位置可以从步骤2开始选在这个半轴。后续把新的有限块放得更右，不改变已选块的坐标。右锚在共同零 collar 内的最终选择不改变原积分，因为全部相关 integrand 在它们的支撑右方为零。

两种弱曲段都在真实 $A_f=0$ 活动区内，内部常项不改变其正阶 jets；宽过渡区 $g=0$，其余补包和控制区为强 hook。原弱条件由局部式与右锚常数准确保持，没有增加第二个 hook。每个三矩基本圆的八副本仍作用于原完整相位第三 range；对镜像 profiles 也使用该原 range，而不是反射原几何。所有种子、初值、两 collar 与完整三阶保持。

## 11. 新增范围

同一个最终真实弱单 hook、导数 rank-two 圆已同时支付：

- 原三矩圆和完整三阶；
- $A_{-2,-3}$ 的全部三个外矩；
- $A_{-1,-3}$ 的全部三个外矩；
- 新 $A_{-1,-2}$ 的完整第零外矩；
- 三条完整 directed 行、$\Psi$ 和指定完整一层(31)；

以上全部对同一 profile、同一几何、全部相位成立。

本稿没有撤销 R337：它确实加入了此前架构禁止的 $C>0$ 弱块，并用最终真实中心与正四次权支付了新增方向。原宽 cutoff、矩补偿及该正块的全部 $\Psi$ 成本均进入构造。

$A_{-1,-2}$ 的第1、第2外矩、其它 Gaussian 面积、其余对称乘积与零／一层函数、canonical 平台／flux、完整第四 period 和同一 gauge 的 joint 仍未由本文完成。目标 metric 在最终新 seed 处固定，不声称维持原 R331 冻结 seed 的目标。
