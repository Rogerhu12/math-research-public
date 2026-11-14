# R133 补篇：完整腰幅度投影，以及最终 ac1 中心的 193 态响应/伴随入口

## 0. 已完成的结论与实际执行范围

本篇只使用最终完整 moving 中心
\[
 {\tt ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413},
 \quad
 \alpha=\frac{6890507429876859}{9007199254740992},\quad
 \nu=-\frac{2572625729470897}{72057594037927936}.                 \tag{H.1}
\]
它的 32 个正频率、全部余弦均值、6145 个径向节点、6144 个真实三次片及
完整区间 \(0\le r\le25/8\) 均不改变。

本次**实际完成并在 V8 执行**的是完整物理腰幅度行的后验消费。使用已经
执行的 96 个余弦列、真实均值列和无限高模尾，得到保均值的幅度右逆
\(\mathcal R\) 与完整幅度核投影 \(\mathcal P\)：
\[
\begin{array}{c|cccc}
 &L^2&H^{1/6}&H^{1/3}&H^1\\ \hline
 \|\mathcal R\| &1147/1000&3/2&37/20&19/4\\
 \|\mathcal P\| &9/5&43/20&13/5&31/5 .
\end{array}                                                       \tag{H.2}
\]
全部界在原 \(\eta\) 盒上成立，均值与所有未知输入频率都保留。
幅度泛函的完整 \(L^2\) 对偶范数小于 \(157/100\)。
以完整整数区间中点构造有限矩阵行，并逐项检查其 binary64 转换后，
**整个真实物理腰行**与该 193 列 proposal 的 \(L^2\) 算子差小于
\[
                          6\,10^{-8}.                            \tag{H.3}
\]
这不是仅有 96 个有限系数的差；已加完整 \(|j|\ge97\) 对偶尾。

程序 fourfold_codazzi_final_head_waist_projection.mjs 实际执行了
22 个精确整数/有理数门。输出在
2026-11-14-R133-final-head-waist-projection-rational.json。
原生没有用浮点平方根或浮点分数幂决定上述任何门。

另外两个新 Python 文件实现完整有限响应和伴随的可恢复入口：

* fourfold_codazzi_final_head_trial_model.py；
* fourfold_codazzi_final_head_trial.py。

**这两个 Python 文件尚未执行，也未在 Python 运行时编译检查。**
当前没有新 M96 径向 trial、QR 成功输出、Schur 符号或全 BVP 逆。
本篇后半给出这些入口所实现的准确方程、单位、投影和后验合同；
不把源码已写成当作实际求解成功。它们不替代已经明确未执行的
whole-positive coefficient/Volterra consumers。

## 1. 真正消费的完整腰数据

输入不是角采样，而是：

1. 2026-11-14-R133-final-waist-complete-96-amplitude-row-rational.json，
   SHA256 c99e3f6c7fd4975ee8fd1de26fadad7f4e42c6c379a861830d6fa419046b052e；
2. 2026-11-14-R133-final-waist-high-amplitude-tail-rational.json，
   SHA256 19fc31617d033a4dcdc92153498592290da23ae58b545f3c5f64dc0ca343a3d9。

两份均绑定 (H.1)、原完整 \(\eta\) 盒和原 32 个有限腰系数。第一份保留
\(2^{384}\) 为分母的完整整数区间；第二份给出整个
\(|j|\ge97\) 的实际中心对偶尾，严格小于 \(10^{-42}\)。
本次实际读取了两份完整文本并独立核对其 SHA256；没有读取或重建二进制
径向缓存。第一份 producer 的 SHA256 为
dc8d3d4183cacc36e617620ca28e7e238564a80a3e53010a39577fe31632d4ae；
第二份 producer 的 SHA256 为
1c5c452613dea03487cb896c0574878954c49fdd3127797373257e610812bd96。

记真实物理腰幅度为 \(\mathcal A(Q)=C_4(0)\)，令
\[
 a_0=D\mathcal A[e_2],\qquad
 a_j=D\mathcal A[(0,\cos4j\phi)]\quad(j\ge1).                       \tag{H.4}
\]
这里是**未 normalized 的 moving \(u,v\) 变分**，不是 \(U,V\) 的系数，
也不是物理梯度函数的余弦幅度。\(D\mathcal A\) 对全部奇分量 \(h_1\)
准确为零。对
\(h_2=z+\sum_{j\ge1}c_j\cos4j\phi\)，
\[
        \ell h_2:=D\mathcal A[h]=a_0z+\sum_{j\ge1}a_jc_j.          \tag{H.5}
\]
真实 \(L^2\) 梯度因此为
\(a_0+2\sum_{j\ge1}a_j\cos4j\phi\)，它的范数平方是
\(a_0^2+2\sum_{j\ge1}a_j^2\)。这个 2 不能从源或乘子中悄然删掉。

完整数据特别给出
\[
\begin{split}
 -.616995919304690416&<a_1<-.616995883004055568,\\
 -1.276023677907614220&<a_0<-1.276023581674613252 .
\end{split}                                                       \tag{H.6}
\]
所有其他列也使用原整数区间，不能只以这两列替代整个泛函。

## 2. 完整保均值右逆与 oblique projection

定义
\[
 \mathcal R t=\frac{t}{a_1}\cos4\phi,\qquad
 \mathcal P=I-\mathcal R\ell .                                    \tag{H.7}
\]
则 \(\ell\mathcal R=1\)、\(\mathcal P^2=\mathcal P\)、
\(\ell\mathcal P=0\)，并且
\[
                 \langle\mathcal R t\rangle=0,\qquad
                 \langle\mathcal P h_2\rangle=\langle h_2\rangle. \tag{H.8}
\]
这给完整腰条件一个显式坐标，不丢弃均值。结合 \(h_1(0)=0\) 时，
整对未知量的腰投影为 \((h_1,h_2)\mapsto(0,\mathcal P h_2)\)。
每个原输入频率都可以进入 (H.5)，并非只在有限头上定义。

设 \(D=2^{384}\)，第一份输入中 \(a_j\) 的整数区间为
\([L_j,U_j]/D\)，置
\[
 p=-U_1>0,\quad b_j=\max(|L_j|,|U_j|),\quad
 S=b_0^2+2\sum_{j=1}^{96}b_j^2,\quad \varepsilon=10^{-42}.          \tag{H.9}
\]
完整 Fourier 正交性给
\[
 |a_1|\ge p/D,\qquad
 \|\ell\|_{(L^2)^*}^2\le S/D^2+\varepsilon^2,\qquad
 \|\mathcal R\|_{\mathbb R\to H^s}^2
       \le\frac{17^sD^2}{2p^2}.                                  \tag{H.10}
\]
高模尾在这里按平方加入；没有把 \(\ell^1\) 或有限格点范数冒充 \(L^2\)。

对任意 Hilbert 空间上满足 \(\ell r=1\) 的 rank-one projection
\(I-r\ell\)，
\[
                       \|I-r\ell\|=\|r\|\,\|\ell\|.              \tag{H.11}
\]
例如在 \(r\) 与 \(\ell\) 的 Riesz 向量张成的二维空间写出投影矩阵，
其唯一非零奇异值就是右式；在正交补上它为恒等，右式由
Cauchy--Schwarz 不小于 1。这同样适用于这里的完整无限维 \(H^s\)。

所有非零频率满足 \(1+16j^2\ge17\)，故
\[
 \|\mathcal P\|_{H^s\to H^s}^2
 \le\frac{
       17^s b_0^2+(S-b_0^2)+17^sD^2\varepsilon^2
      }{2p^2}.                                                   \tag{H.12}
\]
以
\[
 17^{1/6}<401/250,\qquad 17^{1/3}<643/250                          \tag{H.13}
\]
及 \(17^1=17\) 代入，即得到 (H.2)。程序把 (H.13) 分别提升六次、
三次检验；右逆的两个分数阶门也先消去正平方根再提升整数次。
实际对 (H.10)--(H.12) 的比较全是 BigInt 整数交叉乘积。
因而 (H.2) 不是插值时遗漏均值的结果。

这些常数属于当前冻结中心的完整行。未知 Wiener 球的另一个高模尾预算
仍由原输入保留；本篇不把 (H.2) 免费转给改变背景后的 \(D\mathcal A\)。

## 3. 实际有限 proposal 的完整误差

新 head factory 不再以腰部 trapezoidal quadrature 作为幅度矩阵行。
它读取上述全部整数区间，逐项采用
\[
       \widehat a_j=\operatorname{float}
             \left(\frac{L_j+U_j}{2D}\right).                    \tag{H.14}
\]
源码先以 Fraction 构造准确中点，再一次转换到 float；并将 float 准确
转回 Fraction，实际要求每列的转换费不超过 \(2^{-52}\)。
若此检查失败，直接保存失败并拒绝该行。

令 \(t_j=(U_j-L_j)/(2D)+2^{-52}\)，则整个实际物理泛函与零延长的
proposal 的差满足
\[
 \|\ell-\widehat\ell_{96}\|_{(L^2)^*}^2
 \le t_0^2+2\sum_{j=1}^{96}t_j^2+\varepsilon^2<(6\,10^{-8})^2.     \tag{H.15}
\]
最后一个严格有理数门已实际执行；逐个具体 Python float 的转换检查
则属于将来的实际 producer 执行，本文没有伪称已发生。
源码同时保存每列原区间、准确 proposal 误差和完整总误差。
完整物理 boundary consumer 仍对真实泛函作独立全 Fourier 消费；
它不以 (H.14) 当作真实点值。

## 4. 同一中心的完整 Jacobi 主体与真正参数源

写 \(Q=(u,v)\)、\(m=\langle v\rangle\)、
\[
 J=\begin{pmatrix}0&K\\-1&0\end{pmatrix},\quad
 S=u^2+Kv^2,\quad d=-\beta I S,\quad I=\partial_\phi^{-1}P_{\ne0}.
\]
原 moving 方程为
\[
 F_1=d u_\phi+\gamma mK v_\phi-\beta u(1+S),\quad
 F_2=d v_\phi-\gamma m u_\phi+\beta v(1-S).                         \tag{H.16}
\]
不要求保存中心恰好满足 PDE。准确导数为
\[
\begin{split}
 \mathscr A_Q h={}&(dI_2+\gamma mJ)h_\phi+Lh\\
 &-2\beta Q_\phi I(uh_1+Kvh_2)
      +\gamma\langle h_2\rangle JQ_\phi,\\
 L={}&
 \begin{pmatrix}
 -\beta(1+3u^2+Kv^2)&-2\beta Kuv\\
 -2\beta uv&\beta(1-u^2-3Kv^2)
 \end{pmatrix},\qquad
 D_Qh=h_r-\mathscr A_Qh.                                         \tag{H.17}
\end{split}
\]
原完整 primitive 和 rank-one 均值列都在源码中保留。没有除 \(K\)，
故有限代数可以跨真正 turning point；这不自动授予跨点全频 Cauchy 适定性。

设原控制 bump 为 \(w(r)\)，则在**固定物理 moving \(u,v\)** 下
\[
 \gamma_\nu=\gamma w/2,\quad \beta_\nu=0,\quad
 K_\nu=-Kw+\frac{\beta w'}{2a^2\gamma^2}.                          \tag{H.18}
\]
真正响应右端 \(F_\nu=\partial_\nu F|_Q\) 为
\[
\begin{split}
 (F_\nu)_1={}&-\beta K_\nu\{I(v^2)u_\phi+v^2u\}
             +\gamma m(Kw/2+K_\nu)v_\phi,\\
 (F_\nu)_2={}&-\beta K_\nu\{I(v^2)v_\phi+v^3\}
             -\gamma m w u_\phi/2.                              \tag{H.19}
\end{split}
\]
因此本入口求的是 \(D_Qh_\nu=F_\nu\)。
均值源准确为
\[
              \langle(F_\nu)_2\rangle
                    =-\beta mK_\nu\langle v^2\rangle.            \tag{H.20}
\]
它用
\(\langle I(v^2)v_\phi\rangle=-\langle v^3\rangle
 +m\langle v^2\rangle\) 得到。程序把这列与完整 FFT 投影独立比较。

原 normalized solver 的 parameter 列在固定 \(U,V\) 下求导，含
\(s_\nu\) 和参考导数。它不是 (H.19)。
新 factory 明确不用那一列作为物理响应源，而直接实现 (H.19)。
只有状态 Jacobian 可以复用：常量 \(\alpha\) 在
\(\delta Q=\alpha\delta(U,V)\) 与 normalized 方程两侧准确相消。

## 5. 193 态完整有限头和所有 body 头--高耦合

令 \(\Pi_L\) 保留奇分量 \(\sin4j\phi\), \(1\le j\le96\)，
偶分量 \(1,\cos4j\phi\), \(1\le j\le96\)。
实状态维数是 \(96+97=193\)，不是只保一个复 Fourier 锥。

冻结背景的次数仍为 32。对任意次数 \(N\) 的输入，(H.17) 的完整输出
次数最多 \(N+64\)：先作完 \(uh_1+Kvh_2\) 的 \(N+32\) 次乘积和完整 \(I\)，
再乘 \(Q_\phi\)。不能在 primitive 中间提前投回 \(N\)。
因此实际 M96 trial 的完整 body residual 可到 160：
\[
             1\le j\le160,\qquad \text{全部均值另保}.             \tag{H.21}
\]
(H.19) 的完整体源到 96。这正好匹配已有
fourfold_codazzi_mean_completed_head_body_residual.py 的完整输出合同。

直接 body 耦合还有更准确的投影位置：
\[
 \Pi_H\mathscr A_Q\Pi_{\le32}=0,\qquad
 \Pi_{\le32}\mathscr A_Q\Pi_H=0,\quad
 \Pi_H=\Pi_{|j|\ge97}.                                           \tag{H.22}
\]
所有直接 head/high body 项只经过
head 的 \(33\ldots96\) 与 high 的 \(97\ldots160\) 两个 128 维实壳层。
均值不能直接送入 high，高输入也不能直接送入 body 均值。
这**不**意味着高演化被截断在 160；high/high 的反复传播仍在无限多个模式上。
也不意味着真实物理边界有这个有限带宽。

新 head_shell_blocks 逐批构造整个
\(\Pi_H\mathscr A_Q\Pi_L\) 和 \(\Pi_L\mathscr A_Q\Pi_H\) 的上述直接矩阵。
高输入先完整合成到 160，所有中间/输出支持均由原 1024 角网格容纳，
然后才取需要的最终行。其用途是将来组装 Schur 费用，不能直接充当
全高块 Green。本段的有限支持事实只用于冻结 M32 中心；
改变背景的未知无限尾须用已付的任意频比/A³ 邻域合同，不能继承 (H.22)。

## 6. 原物理边界与一个无混淆的辅助标量

有限 proposal 的左边界为 96 个真正 \(u\) 正弦 Dirichlet 行，
加当前准确物理 \(C_4\) 幅度行的 (H.14) proposal。
右边界为真物理 \(C\) 均值行的 proposal，以及原物理 Robin
实余弦幅度行 \(j=2,\ldots,96\)。

原 \(j=1\), 即物理频率 4 的 Robin 行留作输出
\(\widetilde b_4\)。所有右边界均在原物理角 \(\theta\) 中计算；
moving 有限 Fourier 向量不能直接当 physical Fourier 向量。
记这些完整有限边界矩阵为
\[
 B_0\in\mathbb R^{97\times193},\qquad
 B_R\in\mathbb R^{96\times193},\qquad
 \widetilde b_4\in(\mathbb R^{193})^*.                            \tag{H.23}
\]
固定 \(\nu\) 的有限补问题记为 \(\widetilde{\mathcal A}_{LL}\)，
含 \(\Pi_LD_Q\Pi_L\)、\(B_0\)、\(B_R\)。
为复用现有 one-parameter 全行 QR，只再加
\[
                    \widetilde b_4 h(R)+\lambda=0.               \tag{H.24}
\]
这个 \(\lambda\) 在所有体方程、左边界和其他右边界中系数准确为 0，
只在 (H.24) 中系数为 1。它**不是** \(\delta\nu\)。
增广算子及其逆准确为
\[
 \begin{pmatrix}
 \widetilde{\mathcal A}_{LL}&0\\\widetilde b_4&1
 \end{pmatrix},
 \qquad
 \begin{pmatrix}
 \widetilde G_L&0\\-\widetilde b_4\widetilde G_L&1
 \end{pmatrix}.                                                  \tag{H.25}
\]
前者可逆当且仅当原有限补问题可逆。因此增加该标量既不隐藏奇异性，
也不对原低模施加多一个物理条件。
响应解满足 \(\lambda=-\widetilde b_4h_\nu(R)\)。
程序返回的是 proposal 值，不能据此未经后验宣布真实 \(\nu\) Schur 非零。

原 boundary_jet 的归一化约定没有引入额外 \(\alpha\)：
若 \(\widehat C=(C-C_{\rm ref})/\alpha\)，
\(Q=Q_c+\alpha\,\delta y\)，则
\(D_y\widehat C=D_QC\)；\(B/\alpha\) 同理。
参数在两端支持外准确为零，所以本源没有额外显式端点 \(\nu\) 列。
真实 nonlinear DN、物理无限 Fourier 尾和全部 exterior mean
仍由已付的完整 boundary consumer 校正，不能由 proposal 行消失。

## 7. 完整 \(L^2\) 伴随与实际乘子单位

实幅度向量的完整内积矩阵为
\[
 W=\operatorname{diag}\bigl(
 \underbrace{\tfrac12,\ldots,\tfrac12}_{96\ {\rm sine}},
 1,\underbrace{\tfrac12,\ldots,\tfrac12}_{96\ {\rm cosine}}\bigr). \tag{H.26}
\]
故有限 Galerkin 系数的伴随 ODE 为
\[
              \psi_r=-W^{-1}A_L(r)^T W\psi.                      \tag{H.27}
\]
源码还独立实施完整 FFT 形式，避免只用同一个矩阵检查自己：
\[
\begin{split}
 D_Q^*\psi={}&-\psi_r+
       (dI_2+\gamma mJ^T)\psi_\phi+d_\phi\psi-L^T\psi\\
 &-2\beta(u,Kv)\,I(Q_\phi\!\cdot\!\psi)
       -\gamma e_2\langle JQ_\phi\!\cdot\!\psi\rangle .             \tag{H.28}
\end{split}
\]
完整 \(I^*=-I\)、两条均值项及 \(d_\phi\) 都保留。
两种动作与完整 \(W\) 配对将在实际背景点独立检查；
本文没有伪造这些尚未运行的数值检查结果。

对原输出 \(\widetilde b_4h(R)\)，选择伴随端口
\[
 W\psi(0)=B_0^T\lambda_0,\qquad
 W\psi(R)=\widetilde b_4^T-B_R^T\lambda_R.                         \tag{H.29}
\]
在连续解上只需 \(D_Q^*\psi=0\)，便有
\[
 \widetilde b_4h(R)
  =\int_0^R\langle\psi,D_Qh\rangle_\phi\,dr
       +\lambda_0^TB_0h(0)+\lambda_R^TB_Rh(R).                    \tag{H.30}
\]
这里右端减号和左端正号由径向分部积分直接确定。

左端不需要数值 nullspace。令 proposal 幅度列为
\(\widehat a_0,\ldots,\widehat a_{96}\)，由非零的 \(\widehat a_1\)
可显式写出全部 96 条左伴随条件：
\[
 \psi_{2,0}-\frac{\widehat a_0}{2\widehat a_1}\psi_{2,1}=0,\quad
 \psi_{2,j}-\frac{\widehat a_j}{\widehat a_1}\psi_{2,1}=0
                   \quad(2\le j\le96).                          \tag{H.31}
\]
特别地
\[
 \lambda_{\rm amp}=\frac{\psi_{2,1}(0)}{2\widehat a_1},\qquad
 (\lambda_{0,u})_j=\frac{\psi_{1,j}(0)}2.                           \tag{H.32}
\]
均值行的 2 是 (H.26) 的必要结果，不能使用非零频率公式代替它。

右端以完整 \(B_R\) 的 nullspace \(Z_R\) 施加
\(Z_RW\psi(R)=Z_R\widetilde b_4^T\)，并在实际运行中检查完整行秩。
最后从
\(B_R^T\lambda_R=\widetilde b_4^T-W\psi(R)\) 恢复全部右乘子。
为保持同一个 QR 存储协议，伴随只增加一个独立的零 dummy 标量行；
它不参与任何体式或真实端口。

导出的 cosine_amplitude_multipliers 是 physical real-cosine
**幅度行的乘子**。第一项准确为 0，因为物理 \(m=4\) 是原输出，
不是 retained 行。完整 boundary consumer 自行把它组成
\(2\sum\lambda_j\cos4j\theta\)；producer 不预乘 2，也不乘/除 \(\alpha\)。

(H.27) 是连续 Galerkin 微分算子的伴随再作径向 collocation。
它不声称是另一套浮点 collocation 大矩阵的逐字转置。
所有连续 body、boundary、jump 缺陷仍由独立 interval consumer 支付。

## 8. 真正分片系数、完整恢复与输出

背景每个三次片都按其原 dyadic 系数读取。每个新 collocation 区间包含于
一个原片，并分别在该片的左端、中点、右端取值；在接缝处不以右片值
覆盖左片值。令 \(A_0,A_m,A_1\) 为同一片的三个矩阵，长度 \(h\)，
原完整 Lobatto 块为
\[
\begin{split}
 L_i&=-I-\frac h6(A_0+2A_m)-\frac{h^2}{12}A_mA_0,\\
 R_i&= I-\frac h6(A_1+2A_m)+\frac{h^2}{12}A_mA_1,\\
 b_i&=\frac h6(F_0+F_1+4F_m)+\frac{h^2}{12}A_m(F_0-F_1).
\end{split}                                                       \tag{H.33}
\]
\(\lambda\) 的所有体块列准确为零。每个 193×193 项都保留。

实现复用既有完整 boundary-row QR 的 step/read/solve，
新增的只是 factor 前缀恢复。每个短段后先保存不可变完整数组，
再原子保存带 SHA 的指针；未完成的写入不能替代上个完整 generation。
factor、正向代入、反向代入、独立全算子残差、最终 Hermite 输出都可恢复。
输入指纹包含真实候选/原对象/原 q、实际腰区间行、全部依赖源码、版本、
径向节点、角色、角网格及完整边界矩阵。没有 entry dropping 或 band truncation。

每次实际解都保留既有 \(5\,10^{-8}\) **完整浮点 backward residual**
门和最多三次完整 refinement。该门通过仍不等于 continuous inverse。
独立检查使用 (H.17)/(H.28) 的 FFT 动作及全部物理边界行，
不重用 factor 的矩形矩阵动作。每个检验前缀也按准确 answer/RHS 身份保存。

输出三次 Hermite 的两个端导数取**同一原背景片**的真实单侧动作。
完整 trial 的均值先保存；随后只将整条 \(h_2\) mean cubic 列准确置零，
另存供 scalar Green 消费的 trial。所有其他系数逐位保留。
真实 dyadic trial 接缝仍可能非零；已有消费者对每个 join 准确支付。

投影后 metadata 严格遵循既有 read_trial：

* kind 为 actual_final_mean_eliminated_trial_v1；
* role 为 response 或 adjoint_nonmean；
* 当前背景 SHA、准确 \(\alpha,\nu\)、193 列、完整 \([0,25/8]\)；
* 全部 mean cubic 系数准确为 0；
* initial_state 逐位等于 piece_coefficients[-1,0,:]；
* 保存投影前完整 trial 的路径和 SHA。

最终实际外均值、伴随均值、参数源和真实物理边界分别交给
fourfold_codazzi_mean_completed_head_body_residual.py 及
fourfold_codazzi_mean_completed_physical_boundary.py。

finite full trial 的 mean 只作为完整试算/复现记录，不替代这些真 scalar ODE。
原始均值被明确重填后引起的非零模式 residual 会完整进入 body 消费，
不能悄然宣布投影后的 trial 仍解原有限齐次系统。

## 9. 没有消失的真正全高 Schur

在完整固定 \(\nu\) 实现中，按实际 head/high 端口分块：
\[
 \overline{\mathcal A}=
 \begin{pmatrix}\mathcal A_{LL}&\mathcal A_{LH}\\
                 \mathcal A_{HL}&\mathcal A_{HH}\end{pmatrix}.    \tag{H.34}
\]
完整真实外 DN、腰幅度、外均值、ordinary source、真正接缝都属于这些块。
(H.22) 只简化直接 body 交叉项；它没有删除：

* 腰幅度的完整高频行及其已付小尾；
* 外 nonlinear mean 的 high→low finite-rank 路径；
* 所有真实物理 Robin 高行和 head/high composition；
* 高区中的反复全频传播与负侧两端相位条件。

只有当同一端口/源空间中的
\(G_H=\mathcal A_{HH}^{-1}\) 真正付清后，才能使用
\[
 \mathcal S_L=\mathcal A_{LL}
                 -\mathcal A_{LH}G_H\mathcal A_{HL},\qquad
 h_H=G_H(f_H-\mathcal A_{HL}h_L).                                 \tag{H.35}
\]
新有限 QR 直接解的是 proposal
\(\widetilde{\mathcal A}_{LL}\)，不是 \(\mathcal S_L\)。
实际核验必须保留
\[
 \mathcal A_{LL}-\widetilde{\mathcal A}_{LL}
       -\mathcal A_{LH}G_H\mathcal A_{HL}.                         \tag{H.36}
\]
不能由 finite QR condition number、root 局部全逆、positive high gap
或极小的一个 boundary 行误差，单独宣称 (H.36) 可吸收。
目前完整 ac1 正区缓存 producer 仍未执行，负侧/全回路 high 间隙及最终
\(\nu\) scalar 也未因此闭合。

## 10. 可恢复的具体命令

先按已发表的 final-moving replay chain 恢复原 ac1 候选及其五个完整分片，
把实际位置通过 --candidate 给出。不要把已失去的临时路径当现成数据，
也不重复提交这些可快重现的大中间数组。

在课题目录，实际命令形如：

~~~sh
python scripts/fourfold_codazzi_final_head_trial.py \
  --candidate /absolute/restored/ac1-candidate.json \
  --role response --modes 96 --angles 1024 --boundary-angles 8192 \
  --span 8 --max-new-blocks 64 \
  --work /absolute/scratch/ac1-head96 \
  --out /absolute/scratch/ac1-head96-response-run001.json

python scripts/fourfold_codazzi_final_head_trial.py \
  --candidate /absolute/restored/ac1-candidate.json \
  --role adjoint --modes 96 --angles 1024 --boundary-angles 8192 \
  --span 8 --max-new-blocks 64 \
  --work /absolute/scratch/ac1-head96 \
  --out /absolute/scratch/ac1-head96-adjoint-run001.json
~~~

每次后续只换新的 --out 文件名，保持所有模型/网格/源身份不变；
case 指纹决定读取同一完整检查点。paused_after_complete_checkpoint
表示已保存的有界短片，不是数学失败，也不是最终收敛。
任何真实失败均保留原 report，不能覆盖或伪改为成功。

已执行的小有理数消费者可直接重放：

~~~sh
node scripts/fourfold_codazzi_final_head_waist_projection.mjs
~~~

最后再次明确：22 个有理门已经真实执行；两个 Python 入口尚未运行。
本篇闭合的是完整腰投影、proposal 费用与可审阅/可恢复的实际 head/adjoint
实现，不是课题的完成标准。
