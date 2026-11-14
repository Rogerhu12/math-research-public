# R492 — 实际两 Theta 的完整 principal 三张量与双变量中央式

日期：2026-11-14。**状态：已证明。** R490 的两条 degree34/34
联合，在分别取完整 \(\mu_6\) principal 部分后，准确只有三个
张量。整个 \(36\) 维空间中的其余部分由同一个完整 CM7
关系排除，未以边际质量零删掉来源。三个张量的系数全部付清。

这给原 \(J_S'(0)\) 一个准确的双单位反对称积分表达，并给
原 \(C_{26}/\Theta\) 联合的全部 principal 分解。已知非零
参考差与未付的原中央非零仍严格分开。

## 1. 同一个原两输入来源

保 R490 的 \(b=17\)、\(\delta^2=-3\)、\(\omega=(-1+\delta)/2\)、
原 \(\sigma,\Theta=x\sigma^2\) 与所有普通 ray 规范。记
\[
 \gamma=(7+\delta)/2,\qquad \gamma\bar\gamma=13,\qquad
 c=336b\delta,\qquad c_\pm=168b(1\mp\delta).
\tag{1}
\]
这里 \(c_+\) 对应 \(\gamma\)，\(c_-\) 对应 \(\bar\gamma\)。

实际二变量函数是
\[
 H_+(w,z)=\Theta(\gamma w+2z)\Theta(2w-\bar\gamma z),
\quad
 H_-(w,z)=\Theta(\bar\gamma w+2z)\Theta(2w-\gamma z).
\tag{2}
\]
由 R490 的真实整矩阵
\[
 B_+=\begin{pmatrix}\gamma&2\\2&-\bar\gamma\end{pmatrix},
 \qquad B_+B_+^*=17I,\qquad\det B_+=-17,
\]
两来源都在标准完整
\(\mathcal S_{34}\otimes\mathcal S_{34}\)，所有 canonical 相位已付。
令 \(\Pi_w,\Pi_z\) 为各轴完整的 \(\mu_6\) 平均。由于 (2) 在同时
乘 \(\zeta\in\mu_6\) 时不变，
\[
 \Pi_wH_\pm=\Pi_zH_\pm=\Pi_w\Pi_zH_\pm.
\tag{3}
\]
以下只在有 (3) 的这个完整投影之后写三项来源式。

原质量一参考仍为 R308 的
\[
 \begin{aligned}
 H_3&=\sigma^{34}x^2
 (X^5-208bX^4+400b^2X^3+8128b^3X^2+12032b^4X-2048b^5),\\
 H_5&=\sigma^{34}x^2
 (X^5+272bX^4-272b^2X^3-14912b^3X^2-6784b^4X+1024b^5).
 \end{aligned}
\tag{4}
\]
\(S(0)=0,[z^6]S=1\)，而 \(H_3(0)=H_5(0)=1\)。这三条都使用
原同一个周期，未把 \(H_3,H_5\) 换成新的曲线。

## 2. 完整三十六维空间的三维联合特征空间

对 R490 的整个六维 principal 空间
\[
 \mathcal H_{34}^+=\sigma^{34}x^2K[X]_{\le5}
\]
记完整 normalized CM7 矩阵为 \(N\)。该矩阵由真实全部七点
纤维构成。精确恒等式是
\[
 \boxed{(N^3+I)(N^3+\omega I)=0.}
\tag{5}
\]
两个三次块各维三；在 \(N^3=-1\) 的块中，
\[
 NS=-S,\qquad NH_3=-\omega H_3,\qquad NH_5=-\omega^2H_5
\tag{6}
\]
是三个各自一维的完整特征线。相应三维投影为
\[
 E=\frac{N^3+\omega I}{\omega-1}.
\tag{7}
\]
全部恒等式、幂等性与维数都在附脚本的精确有理数域中计算，
未从几个非零特征向量推断整个空间。

R490 的完整双纤维重排已给
\[
 (N_wN_z)H_\pm=\omega^2H_\pm.
\tag{8}
\]
它与两个角平均交换，所以也对 (3) 成立。取三次方得
\(N_w^3N_z^3=1\) 于该实际来源。在 (5) 的两块上，两个因子的
可能三次特征为 \(-1,-\omega\)。除 \((-1,-1)\) 之外，其乘积
为 \(\omega\) 或 \(\omega^2\)，均不为一。因此 (3) 必在
\(E\mathcal H_{34}^+\otimes E\mathcal H_{34}^+\) 内。

再用 (6)、(8)，唯一允许的三个张量为
\[
 \boxed{H_3(w)H_3(z),\qquad S(w)H_5(z),\qquad H_5(w)S(z).}
\tag{9}
\]
附脚本还直接在整个 \(6\otimes6\) 空间核得
\[
 \operatorname{rank}(N\otimes N-\omega^2I)=33
\]
以及 (9) 的秩为三。所以这确为整个联合特征空间，没有遗漏
边际质量为零的其他张量。

## 3. 三个系数与完整 addition 身份

R490 的完整 norm13 多项式乘 \(\Theta(2w)\) 后，不仅能算一个
秩一投影；整个一变量式已经准确为
\[
 \boxed{H_+(w,0)=H_3(w)+c_+S(w),\qquad
        H_-(w,0)=H_3(w)+c_-S(w).}
\tag{10}
\]
这是六个全部多项式系数的身份，附脚本逐项验证。一般 \(b\) 下
\(c_\pm\) 恰为 (1) 的一次 \(b\)，不删这一实际尺度。

将 \(z=0\) 代入 (9)，可读出 \(H_3\otimes H_3\) 的系数为一，
\(S\otimes H_5\) 的系数分别为 \(c_+,c_-\)。
第三个系数不能从该边际读出，因为 \(S(0)=0\)。它由整个函数
的准确交换式确定：
\[
 H_+(z,w)=H_-(w,-z).
\tag{11}
\]
证明只需交换两个相同 \(\Theta\) 因子并使用其偶性。相应矩阵
身份的第二个原 \(\Theta\) 因子有一个负号，脚本完整保留这个
行符号；没有把矩阵本身误称为无符号交换。

(3) 在各轴均为偶，故 (11) 交换后给剩余系数。最终得到
\[
 \boxed{\begin{aligned}
 \Pi_wH_+
   &=H_3(w)H_3(z)
     +c_+S(w)H_5(z)+c_-H_5(w)S(z),\\
 \Pi_wH_-
   &=H_3(w)H_3(z)
     +c_-S(w)H_5(z)+c_+H_5(w)S(z).
 \end{aligned}}
\tag{12}
\]
特别
\[
 \boxed{\Pi_w(H_--H_+)
     =c\bigl(S(w)H_5(z)-H_5(w)S(z)\bigr).}
\tag{13}
\]
(12) 是完整 theta 来源身份；无需对任意目标素数作采样验证。

## 4. 两个真实输出的完整 Mellin 身份

设物理输入 \(X_1,X_2\) 携带两个原独立 \(\nu_\Theta\)。
对 \(H_+\)，相应两个真实输出为
\[
 W=\gamma X_1+2X_2,\qquad Z=2X_1-\bar\gamma X_2.
\tag{14}
\]
它们的 degree 各为 \(34\)，坐标矩阵的 determinant 为 \(-17\)。
\(H_-\) 取 \(\gamma,\bar\gamma\) 互换的另一对完整输出。

记 \(d_p=p-1\)，以及原一变量函数
\[
 J_F(s)=\int_{\mathbf Z_p^\times}\langle x\rangle^{d_ps}\,d\nu_F(x).
\]
定义真正的双单位积分
\[
 \mathcal F_\pm(s,t)
 =\int_{W,Z\in\mathbf Z_p^\times}
     \langle W\rangle^{d_ps}\langle Z\rangle^{d_pt}\,d\nu_{H_\pm}.
\tag{15}
\]
单位域和两个权都在各自的 \(\mu_6\) 单位作用下不变，
所以 (15) 可以使用 (12)，无需给其他角特征赋中央零。
整个两变量解析函数恰为
\[
 \boxed{\begin{aligned}
 \mathcal F_+(s,t)
  &=J_3(s)J_3(t)+c_+J_S(s)J_5(t)+c_-J_5(s)J_S(t),\\
 \mathcal F_-(s,t)
  &=J_3(s)J_3(t)+c_-J_S(s)J_5(t)+c_+J_5(s)J_S(t).
 \end{aligned}}
\tag{16}
\]
其中 \(J_3,J_5\) 分别是 (4) 的完整 Mellin 函数。
这不是把乘积来源的 Mellin 错当一变量乘积；乘积在两个实际
独立输出坐标上已经由 (12) 分离。

原 whole \(K_{34}\) 是反射。因 (4) 和 \(S\) 都为偶，
\[
 J_S(0)=0,\qquad J_3(0)=J_5(0)=1-\lambda.
\tag{17}
\]
由 (16) 得
\[
 \mathcal F_-(s,t)-\mathcal F_+(s,t)
 =c\bigl(J_S(s)J_5(t)-J_5(s)J_S(t)\bigr),\qquad
 \mathcal F_-(s,t)=\mathcal F_+(t,s).
\tag{18}
\]
特别原中央导数的准确入口为
\[
 \boxed{
 (\partial_t-\partial_s)\mathcal F_+(0,0)
   =c(1-\lambda)J_S'(0).}
\tag{19}
\]
将 (15) 写回同一个原输入，就是
\[
 \boxed{
 J_S'(0)=
 \frac{d_p}{336b\delta(1-\lambda)}
 \int_{\substack{\gamma X_1+2X_2\in\mathbf Z_p^\times\\
                  2X_1-\bar\gamma X_2\in\mathbf Z_p^\times}}
 \log\left\langle
       \frac{2X_1-\bar\gamma X_2}{\gamma X_1+2X_2}
      \right\rangle
 \,d\nu_\Theta(X_1)d\nu_\Theta(X_2).}
\tag{20}
\]
全部两个单位条件都在 (20) 中，不能只保其中一个。
分母在当前位是单位；(20) 的非零严格等价原 \(J_S'(0)\ne0\)。

参考未知导数的完整位置也明确为
\[
 \begin{aligned}
 \partial_s\mathcal F_+(0,0)
   &=(1-\lambda)(J_3'(0)+c_+J_S'(0)),\\
 \partial_t\mathcal F_+(0,0)
   &=(1-\lambda)(J_3'(0)+c_-J_S'(0)),\\
 \partial_s\partial_t\mathcal F_+(0,0)
   &=J_3'(0)^2+336b\,J_S'(0)J_5'(0).
 \end{aligned}
\tag{21}
\]
(19) 消去了同一个 \(J_3'(0)\)，没有给它赋零。

## 5. 所有双环带及完整归一

对 \(n,m\ge0\)，将 (15) 的域换成
\(W\in p^n\mathbf Z_p^\times,\ Z\in p^m\mathbf Z_p^\times\)，
两个权分别按 \(W/p^n,Z/p^m\) 归一，记为
\(\mathcal F_\pm^{n,m}(s,t)\)。整个双张量 core 及各轴反射给
\[
 \boxed{\mathcal F_\pm^{n,m}(s,t)
 =\lambda^{n+m}
   \langle\lambda^2\rangle^{d_p(ns+mt)}\mathcal F_\pm(s,t).}
\tag{22}
\]
可从 (12) 的三个完整 scalar 张量逐项证明，也可直接用 whole
两个 degree34 核；反射在这些权下无影响。

特别
\[
 \mathcal F_\pm(0,0)=(1-\lambda)^2 .
\tag{23}
\]
若比较不同 \(n,m\) 的反对称一阶观察，(22) 必须保留
\[
 d_p(m-n)\log\langle\lambda^2\rangle(1-\lambda)^2
\]
这一非齐次尺度项。它不是新的 \(J_S'\) 非零证明。本文只逐个
使用有限环带恒等式，不将 \(p\)-adic 单位比 \(\lambda\) 的无限
几何级数当作自动收敛。

## 6. 原 C26/Theta 联合的全部 principal 分解

返回 R490 的真实两输入
\[
 \Phi(w,v)=C(w+2v)\Theta(2w-13v).
\]
该文整个身份为
\[
 \Phi(w,v)=\frac{H_-(w,\bar\gamma v)-H_+(w,\gamma v)}{c}.
\tag{24}
\]
定义完整一变量来源
\[
 \begin{aligned}
 C_3(v)&=\frac{H_3(\bar\gamma v)-H_3(\gamma v)}c,\\
 C_S(v)&=\frac{(1-\delta)S(\bar\gamma v)
                    -(1+\delta)S(\gamma v)}{2\delta},\\
 \Lambda(v)&=\frac{(1+\delta)H_5(\bar\gamma v)
                    -(1-\delta)H_5(\gamma v)}{2\delta}.
 \end{aligned}
\tag{25}
\]
\(\Lambda\) 是 R490 已付的原 degree442 伴随，未换来源。
将 (12) 逐项代入 (24) 得
\[
 \boxed{\Pi_W\Phi
     =H_3(W)C_3(V)+S(W)\Lambda(V)+H_5(W)C_S(V).}
\tag{26}
\]
整个 \(\Pi_W\Psi\) 亦相同。因为 (24) 同时 \(\mu_6\) 不变，
(26) 也已是两输出各自的完整 principal 部分。

三个伴随均为实际整来源，核心都是 \(\lambda\)，质量分别为
\(0,1,0\)。它们的完整 Mellin 函数是
\[
 \begin{aligned}
 J_{C_3}(t)&=
 \frac{\langle\bar\gamma\rangle^{d_pt}
       -\langle\gamma\rangle^{d_pt}}c\,J_3(t),\\
 J_{C_S}(t)&=
 \frac{(1-\delta)\langle\bar\gamma\rangle^{d_pt}
       -(1+\delta)\langle\gamma\rangle^{d_pt}}{2\delta}\,J_S(t).
 \end{aligned}
\tag{27}
\]
因此
\[
 \boxed{
 J_{C_3}'(0)=
 \frac{d_p\log\langle\bar\gamma/\gamma\rangle(1-\lambda)}c\ne0,
 \qquad J_{C_S}'(0)=-J_S'(0).}
\tag{28}
\]
非零理由已由 R490 的实际 norm13 素理想赋值证明。
未知 \(J_3'(0)\) 在第一式中乘零质量，因此确实消失。

(26) 给整个双单位 Mellin 式
\[
 \boxed{
 \mathcal M_\Phi(s,t)
 =J_3(s)J_{C_3}(t)+J_S(s)J_\Lambda(t)+J_5(s)J_{C_S}(t).}
\tag{29}
\]
在 \(W=0\) 的实际第二边际
\(B(v)=C(2v)\Theta(13v)\) 中，(26) 准确回到
\[
 B=C_3+C_S.
\tag{30}
\]
故 R490 的非齐次式 \(J_B'+J_S'=J_{C_3}'\) 已有整个来源级分解，
而非只在一阶中央处相等。

## 7. 保留的实际缺口

原 \(J_S'(0)=0\) 精确使 (20) 的双单位反对称积分为零，
并使 (28) 的 \(J_{C_S}'(0)=0\)。它仍允许实际
\(J_{C_3}'(0)\ne0\)。完整 (26) 中的这项带原 \(H_3\) 第一来源，
不能从 \(S\) 的中央零删除。

在原 \(C/\Theta\) 输入中，第一输入条件
\(A\in\mathbf Z_p^\times\) 写为
\((13W+2V)/17\in\mathbf Z_p^\times\)。
它不是两个独立输出的 \(\mu_6\)-不变乘积测试。
所以 (29) 不允许把 (27) 的非零项直接替换成
R490 的原 \(A\) 中央观察；同样保留反卷积造成的
\(A,D\mapsto A+2t/17,D-t/17\)。

(20)、(26) 与 (29) 是新的完整接口。证明原反对称积分在无穷
多个 \(p\) 非零，或用另一个真实恒等式消去其完整补域，仍需
继续。本文未从有限维特征计算推出跨 \(p\) 的中央非零。

## 8. 证书和依赖

- [完整三十六维张量核、全部系数及原交换行符号](../scripts/check-r492-complete-principal-two-theta-kernel.py)；
  [精确数据](../scripts/check-r492-complete-principal-two-theta-kernel.json)。
- [R490：实际 norm13 因子、原两输出及 H5 伴随](R490-degree26-cm-difference-and-explicit-h5-companion.md)。
- [R308：H3/H5 的原算术来源、质量与周期](R308-jzero-rank-zero-reference-full-pcore-and-central-masses.md)。
- [R464：完整 CM7 纤维算法](R464-fixed-delta-division-source-full-arithmetic-projection-and-core.md)。

