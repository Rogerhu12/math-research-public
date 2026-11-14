# R342：同一原 Gaussian 重标与 Miller 配对的固定三挠残数

日期：2026-11-13。**状态：以下同一原有限矩阵的准确重分解、完整 Newton 函数的全权重标、Miller forcing 的双 Euler 转置，以及原指定分支上的有限有理残数表达均已证明。最后的残数在一条固定椭圆曲线的三挠单位上读取，测试函数保留全部 \(p\) 依赖；没有把总迹、裸 Cartier 或非零单位本身替代原 \(C_2(M)\) 中的指定配对。**

## 1. 同一原矩阵中的准确 Gaussian 重分解

保留 R338 的 \(p=6s-1\)、\(s>13\)、\(1\le\ell<s-13\)、\(L=2s+\ell\)、
\(b=17\)，以及 R335 整个 canonical 来源、原映射
\[
J:\mathcal V_D\longrightarrow\Gamma_L,\qquad
M=m_{13}J:\mathcal V_D\longrightarrow\Gamma_{L+13}.
\]
原权仍为相对次数加40，两个十三行跨界带和真正的二阶目标
\[
C_2(M)=\operatorname{coker}(\bar M)/\beta_1^M(K_1(M))
\tag{1}
\]
均不改变。沿 R334 记
\[
\kappa=34[w^s]\log(\sigma/z),\quad a_p=p\kappa,\quad
g=e^{-\kappa w^s}\rho,\quad
\mathcal L(t)=\log\Theta^{17}=\sum\ell_nt^n,
\]
\[
\alpha_p=p\ell_s,\qquad d_p=\ell_s-\kappa(-1/b)^s\in\mathcal O.
\]
令
\[
\boxed{\Delta=(-b)^s d_p,\quad
\kappa_*=\kappa+\Delta=(-b)^s\ell_s,\quad
a_*=p\kappa_*=(-b)^s\alpha_p,\quad
g_*=g\,e^{-\Delta w^s}.}
\tag{2}
\]
这里 \(a_*/a_p\in1+p\mathcal O\)，两者均为单位。

**命题1。** (2) 是同一原矩阵的准确重分解：
\[
\boxed{g_*e_2(a_*\epsilon)=g e_2(a_p\epsilon)
\quad\text{于每个已付三块目标中}.}
\tag{3}
\]
整个 canonical 来源的 \(J,M\)、全部精度核、完整 Schur 块及 (1) 逐项不变。
共同 \(G_0\) 的 charge40 单位也不变。

证明是 \(w^s=p\epsilon,\epsilon^3=0\)，所以
\[
e^{-\Delta w^s}e_2((a_p+p\Delta)\epsilon)
=e_2(-p\Delta\epsilon)e_2((a_p+p\Delta)\epsilon)
=e_2(a_p\epsilon).
\]
对各相对 charge 及共同 charge40 取幂即可。这里没有改变来源，也没有删掉 \(m_{13}\)。

## 2. 完整中央函数的重标：整数权、收敛及质量

有限式 (3) 不代替完整中央函数的证明。对实际 \(S(z)=z^6+\cdots\)，置
\(d=p+1=6s\)，
\[
\widehat S_\kappa=e^{-\kappa z^d}S=\sum\gamma_mz^m,\qquad
J_\kappa(u)=\sum_{h\ge0}\kappa^{-h}\gamma_{dh}(u)_h.
\tag{4}
\]
这是 R301/R303 已比较的原完整半因子。

**定理1。**
\[
\boxed{J_{\kappa_*}(u)=(\kappa/\kappa_*)^uJ_\kappa(u),\qquad
J'_{\kappa_*}(0)=J'_\kappa(0).}
\tag{5}
\]
第一式在共同解析圆盘成立，特别在整个 \(u\in\mathbf Z_p\) 上；第二式使用原 \(S(0)=0\)。

**证明。** R301 的半径为 \(R=p^{-1/(2p)}\)。因为 \(\Delta\in\mathcal O\) 且
\(d/(2p)>1/(p-1)\)，\(e^{-\Delta z^d}\) 及其逆在该圆盘实际解析、Gauss 范数为一。
故 R301 的 \(\|\widehat S_\kappa\|_R\le R^6\) 对 \(\kappa_*\) 仍成立，且
\(v_p(\kappa_*)=-1\)。新的全部 Newton 系数仍满足
\[
v_p\!\left(\kappa_*^{-h}[z^{dh}]\widehat S_{\kappa_*}\right)
\ge\left\lceil\frac{h(p-1)+6}{2p}\right\rceil.
\tag{6}
\]
所以原完整 Newton 尾及导数尾保持收敛，未只比较有限中央权。

对每个非负整数 \(k\)，有限卷积准确给
\[
J_\kappa(k)=k!\kappa^{-k}[z^{dk}]S,\qquad
J_{\kappa_*}(k)=k!\kappa_*^{-k}[z^{dk}]S.
\tag{7}
\]
展开 Gaussian 后，内和为
\(\sum_{j=0}^{k-r}(-1)^j\binom{k-r}{j}\)，只保留 \(r=k\)；\(k=0\) 也包括在内。
又 \(\kappa/\kappa_*\in1+p\mathcal O\)，其 \(u\) 次幂在所需圆盘解析。
更明确地，该指数的半径至少为 \(p^{1-1/(p-1)}\)，严格大于
R301 的 \(p^{(p-1)/(2p)}\)。
由 (7) 和非负整数的稠密性，得到 (5) 第一式。求导并用 \(J_\kappa(0)=0\) 得第二式。
\(\square\)

对一个已另行付全 Newton 收敛、质量为 \(m\) 的来源，准确公式则为
\[
J'_{\kappa_*,F}(0)=J'_{\kappa,F}(0)+m\log_p(\kappa/\kappa_*).
\tag{8}
\]
因此没有给 canonical 新列附加中央零。

## 3. 固定 Miller forcing 的双 Euler 原函数

沿 R334 取
\[
h(t)=\sum_{n\ge0}\frac{(1/2)_n}{n!(6n+1)}t^n,\quad
z=x^{-1/2}h(t),\quad t=-b/x^3,\quad
\mathfrak h(w)=h(t(w))=z\sqrt{x(z)},\quad
\mathsf E=6w\partial_w.
\]
保留同一个固定 \(\mathcal T\) 及
\[
\mathcal F=\log h+\frac13\log\frac{1+\sqrt{1-t}}2,\qquad
(1+6t\partial_t)\mathcal T=-(1-t)^{-1/2}\mathcal F.
\]
定义
\[
\boxed{U(w)=\mathcal T(t(w))/h(t(w)).}
\tag{9}
\]
本篇 \(U\) 是 forcing 级数，不是 R320 的 theta 参考 \(\Theta(z)\Theta(2z)^4\)。

由 \(h+6th'=(1-t)^{-1/2}\) 及 R334 的 \(\mathcal F'_z=1/z-\sqrt x\)，准确有
\[
\boxed{(1+\mathsf E)U=-\mathcal F,\quad
\mathsf E\mathcal F=1-\mathfrak h,\quad
\mathsf E(1+\mathsf E)U=\mathfrak h-1.}
\tag{10}
\]
因此 \(U(0)=0\)，且若 \(\mathfrak h=1+\sum_{n\ge1}h_n^*w^n\)，
\[
\boxed{[w^n]U=\frac{h_n^*}{6n(6n+1)}.}
\tag{11}
\]
例如 \(\mathfrak h=1-bw/14+\cdots\)，故 \(U=-bw/588+\cdots\)。
R338 所需 \(n<s-13\)，以及下文中央配对所需 \(n<s\)，显示分母均为 \(p\) 单位。

置
\[
Q_s(t)=\log(1+8t)+\sum_{1\le n<s}\ell_nt^n,\qquad
H_{\rm comp}(w)=\mathscr S(Q_s(t(w))).
\]
R338 的低轴 \(g_<\) 不受 (2) 影响。写 \(g_*=g_<e^{w^sH_*}\)，用
\[
(t/w)^s=(-b)^sh^{-p-1}\equiv(-b)^sh^{-1}\pmod{p,t^s}
\]
及 R338 的完整高轴式，得到
\[
\boxed{\bar H_*=\bar H_{\rm comp}+\bar a_*\bar U\pmod{w^s}.}
\tag{12}
\]
这是同时改 \(g,a_p\) 后的同一原矩阵，未单独删掉 \(d_p\)；
第一项仍保留低 \(t\) 轴重新组合到 \(w\) 轴的全部进位。

## 4. 整个原 \(C_2(M)\) 中的准确对偶系数

取 \(\bar P\in\ker\beta_1^M\) 及其一个原模 \(p^2\) 核提升。
R338 的两条耦合接触尾为
\[
B_1=a_*^{-1}[\mathscr S\bar W_0]_{<s},\qquad
B_2=[\mathscr S\bar W_1]_{<\ell}.
\tag{13}
\]
它们仍来自同一个原 \(P,\mathcal EP\)。取 \(\lambda\in C_2(M)^\vee\)，
将其看作 \(W'/p\) 上同时杀掉实际像和完整首 Bockstein 像的泛函，
记 \(\lambda_{i,r}=\lambda(\epsilon^iw^r)\)。

对有限多项式 \(B\)，定义
\[
\mathcal A_jB=\sum_{r=0}^{j-1}
 \frac{[w^r]B}{6(j-r)(6(j-r)+1)}w^r.
\]
由 (11)，
\[
[w^j](UB)=[w^j]\bigl((\mathfrak h-1)\mathcal A_jB\bigr).
\tag{14}
\]
这是对偶系数转置，不将 \(\mathcal A_jB\) 加入原来源。

置 \(K=s-14\)，定义
\[
\boxed{q_n(\lambda,P)=\frac1{6n(6n+1)}
\left(
\sum_{j=n}^{s-14}\lambda_{1,j+13}[w^{j-n}]B_1+
\sum_{j=n}^{\ell-1}\lambda_{2,j+13}[w^{j-n}]B_2
\right),\quad1\le n\le K.}
\tag{15}
\]
空和为零。两个 \(+13\) 和第一个上界恰来自真正的 \(m_{13}\)。
于是
\[
\boxed{\lambda\!\left(\bar m_{13}(U(0,B_1,B_2))\right)
=\sum_{n=1}^{K}q_n(\lambda,P)h_n^*.}
\tag{16}
\]
原高轴对二阶微分的全部贡献，还须加
\(-\lambda(\bar m_{13}(H_{\rm comp}(0,B_1,B_2)))\)，
并把 (16) 乘以 \(-\bar a_*\)。
本节没有退回未经首提升再商的目标，也没有自由选择两条接触尾。

## 5. 原椭圆对数的有限有理 Frobenius 原函数

以下在同一特征 \(p\) 曲线上工作，各系数均由显示的 \(p\) 整有理数约化。
置
\[
n_0=(p-1)/2=3s-1,\qquad N=3n_0+1=(3p-1)/2,
\]
\[
\boxed{\mathscr R_p(x)=\frac12\sum_{j=0}^{n_0}
 \binom{n_0}{j}b^{\,n_0-j}\frac{x^{3j+1}}{3j+1},
\qquad Z_p=\mathscr R_p(x)/y^p.}
\tag{17}
\]
因 \(p\equiv2\pmod3\) 且 \(3j+1\le N<2p\)，全部分母均是 \(p\) 单位。
准确有
\[
\mathscr R_p'(x)=\tfrac12(x^3+b)^{(p-1)/2},\qquad
\boxed{dZ_p=dx/(2y)=dz\quad\text{于特征 }p.}
\tag{18}
\]
同一特征零有理函数的第一误差也完全保留：
\[
\boxed{\frac{dZ_p}{dz}
=1-\frac{3p x^2\mathscr R_p(x)}{y^{p+1}}.}
\tag{19}
\]

在原支 \(u=x^{-1/2}\)、\(y=-u^{-3}\sqrt{1+bu^6}\) 上，
\(Z_p=u+\cdots\pmod p\)，且与原 \(z(u)\) 一样只含 \(u^{6j+1}\)。
两者差的导数由 (18) 为零，只能含 \(u^{kp}\)；
条件 \(kp\equiv1\pmod6\) 的第一个正解是 \(k=5\)。
R324 已付原 \(z(u)\) 在该窗口整，故
\[
\boxed{z(u)\equiv Z_p(u)\pmod{p,u^{5p}}.}
\tag{20}
\]
这覆盖 (16) 和下文中央配对全部系数。
\(Z_p\) 是 \(p\) 依赖的有理函数，未成为固定小次数来源。

全部有限零极也可核清。若 \(r^3=-b\)，
\[
\boxed{\mathscr R_p(r)=
\frac r2 b^{n_0}\frac{n_0!}{(4/3)_{n_0}}\ne0.}
\tag{21}
\]
这里用
\(\sum(-1)^j\binom nj/(3j+1)=n!/(4/3)_n\)；
它由 \(I_n=\int_0^1(1-v^3)^n\,dv\) 的
\((3n+1)I_n=3nI_{n-1}\) 递推直接证明。
模 \(p\) 的分母因子依次从 \(2s+1\) 到 \(5s-1\)，均为单位。
所以 \(\mathscr R_p\) 在 \(y=0\) 没有根，由 (18) 的多项式导数可知其平方自由。
它在 \(x=0\) 有简单根；三个非零二挠点是 \(Z_p\) 的准确 \(p\) 阶极。
所有这些点保留在 (17) 中。

## 6. 保单原分支的 Miller 残数与固定三挠下降

取 R334 的
\[
\mathscr C:y^2=v^6+b,\quad x=v^2,\quad
f=v^3-y,\quad d\log f=-3v\,dz.
\]
\(P_-\) 表示原支 \(v\sim z^{-1},y\sim-z^{-3}\)。
由 \(h_n^*=[z^{6n}](zv)\)，
\[
h_n^*=\operatorname{Res}_{P_-}z^{-6n}v\,dz.
\]
若 \(6n<5p-1\)，(20) 保证换成 \(Z_p\) 不改变留数。因此
\[
\boxed{\sum q_nh_n^*
=-\frac13\operatorname{Res}_{P_-}
 \left(\sum q_nZ_p^{-6n}\right)d\log f.}
\tag{22}
\]
形式对数已经消去；完整椭圆对数 frame 由准确的 \(Z_p\) 支付。

再取固定椭圆商
\[
E':Y^2=X^3+b^2,\quad X=b/v^2,\quad Y=by/v^3,\quad
Q_\pm=(0,\pm b),\quad r=\frac{Y-b}{Y+b}.
\tag{23}
\]
它是 \((v,y)\mapsto(-v,-y)\) 的商。直接核得
\[
f^2=br,\qquad \operatorname{div}(r)=3(Q_+-Q_-),\qquad
d\log r=\frac{3b}{XY}\,dX.
\tag{24}
\]
\(P_-\) 映到 \(Q_-\)，局部 \(X\sim bu^2\)，分歧指数为二。

写 \(\widetilde{\mathscr R}_p(X)=X^N\mathscr R_p(b/X)\)。
它是 \(X^3\) 的多项式，次数 \(N-1\)，常数项 \(b^N/(2N)\)。
准确的下降函数仅依赖 \(X\)：
\[
\boxed{T_p(X)=Z_p^2=
\frac{X\,\widetilde{\mathscr R}_p(X)^2}
 {b^p(X^3+b^2)^p},\qquad
T_p(X)=X/b+O(X^4)\quad\text{在 }Q_\pm.}
\tag{25}
\]
由 (24) 的 \(1/2\) 与局部分歧指数二准确抵消，(22) 成为
\[
\boxed{\sum q_nh_n^*
=-\frac13\operatorname{Res}_{Q_-}
 \left(\sum q_nT_p(X)^{-3n}\right)d\log r.}
\tag{26}
\]
(15)、(26) 正是原 \(C_2(M)\) 中指定 Miller forcing 的有限有理表达，
未新增 theta 来源。

为保全极点，\(T_p\) 在三处二挠点各有 \(2p\) 阶极；
在 \(Q_\pm\) 各有一阶零，在无穷点有四阶零；
\(\widetilde{\mathscr R}_p\) 的其余根在两个 \(Y\) 分支各给二阶零。
这些由 (17)、(21)、(25) 直接得到。
乘 \(T_p^{-3n}\) 后，原二挠极成为零，但所有显示的 \(T_p\) 零成为真正测试极。

尤其 \(Y\mapsto-Y\) 固定 \(T_p\) 而将 \(d\log r\) 变负。
\(Q_+\) 与 \(Q_-\) 的留数相反，其余成对点也相消。
总残数或 \(\operatorname{Norm}_{T_p}r\) 的这种消去不能读取指定 \(Q_-\)；
(26) 始终保留原支。没有把 \(z\sqrt{x}\) 的两个分支平均掉。
事实上 \(r(X,Y)r(X,-Y)=1\)，所以经 \(k(X)\) 的范数传递直接给
\(\operatorname{Norm}_{k(E')/k(T_p)}r=1\)。这个全局等式正是上述配对相消，
不迫使 (26) 的单分支留数为零。

## 7. 原中央下一位在同一残数族中的位置

令
\[
\widehat S_< =g_<a(t)/(7b)=w+\cdots,\quad
c_1=[w^s]\widehat S_<,\quad c_{2,<}=[w^{2s}]\widehat S_<.
\]
(5)、(6) 使原完整失败在新规范下仍准确给
\[
c_1\equiv0\pmod p,\qquad
a_*c_1-pc_{2,*}\equiv0\pmod{p^2},
\tag{27}
\]
其中 \(c_{2,*}=[w^{2s}](e^{-\kappa_*w^s}S)\)。
由 (12) 和零质量，因而有
\[
\boxed{[w^s](\bar U\,\overline{\widehat S_<})
=\overline{c_1/p}
-\bar a_*^{-1}\left(\overline{c_{2,<}}
+[w^s](\bar H_{\rm comp}\,\overline{\widehat S_<})\right).}
\tag{28}
\]
这里 \(c_1/p\) 仍是原真实下一位；没有分别令两个中央权为零。

左边也由 (26) 读取，其准确测试系数为
\[
\boxed{q_n^{\rm cent}
=\frac{[w^{s-n}]\overline{\widehat S_<}}{6n(6n+1)},
\qquad1\le n\le s-1.}
\tag{29}
\]
即
\[
[w^s](\bar U\,\overline{\widehat S_<})
=-\frac13\operatorname{Res}_{Q_-}
\left(\sum_{n=1}^{s-1}q_n^{\rm cent}T_p^{-3n}\right)d\log r.
\tag{30}
\]
这些 \(\widehat S_<\) 系数都低于首坏轴，正是原 \(S\) 的相应系数。

因此原完整失败给出 (30) 的一条指定值等式。
整个二阶提升读取的是 (15) 所给、受同一原 \(P\) 和真实 \(C_2(M)^\vee\) 限制的测试。
从前者推出后者的像成员性，还须这两类具体测试之间的原关系；
成对残数的总消去不提供它。
后继可以直接在固定 \(E'\)、三挠单位 \(r\) 与完整 \(T_p\) 上研究这个剩余配对。

## 固定精确证书

- [check-jzero-gaussian-miller-adjoint-residue.py](../scripts/check-jzero-gaussian-miller-adjoint-residue.py)
  及其 JSON：核同一矩阵的 Gaussian 恒等式、完整整数权卷积、
  双 Euler 转置、(19) 的第一误差，以及固定三挠下降和全部尺度。
- 只有固定符号恒等式及有限形式代数检查，没有扫描目标素数。

依赖：R301 完整解析圆盘与 Newton 尾；R324 实际有限整性；
R334 固定 Miller forcing；R335 整个原 canonical 来源；
R338 原第二 Bockstein 的完整目标和全部边界。

