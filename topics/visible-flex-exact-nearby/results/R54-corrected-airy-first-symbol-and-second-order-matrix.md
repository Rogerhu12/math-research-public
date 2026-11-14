# R54：校正Airy传播的完整首符号与二阶矩阵余项

2026-11-12，visible-exact-astra-f6a2。

**状态：同一真实canonical组件的已证明中间结论，实际候选输入仍须供应。**
本篇完成R53末尾留下的固定strict cut矩阵提取。共同根剪切后的真实负侧传播，
等于R43同一个自伴首相位加二阶强余项；结论包含幅度两支、正负角频和均值。
与R53的真实正帽接合时不会重新引入原来的4/3阶根误差。

这里所有常数都给出有限Fourier包络公式。它们较粗，不声称当前数值图已经有
可用的截止规模、完整反馈逆或精确闭合族。普通源沿用真实Cauchy/Poisson接触，
不能由齐次首符号的改善替代。

## 1. 输入、记号和结论

沿用R53的实际算子
\[
 L_V=\partial_\xi^2-\xi\partial_\phi^2+V,\qquad
 0\le\xi\le\delta\le1,\qquad \phi\in\mathbb R/\ell\mathbb Z,\quad q=2\pi/\ell.
\]
仍使用完整自由frame \(F_*\)、\(c=c_A^{-1/2}\)、R53的真实实函数 \(B,C\)，
以及准确根剪切
\[
 Q_0=F_*(0)^{-1}
 \begin{pmatrix}I&\Gamma^{-1}M_{V(0)}\Gamma^{-1}\\0&I\end{pmatrix}F_*(0).
\]
频率 \(\lambda_j=q|j|\) 对 \(j\ne0\)，\(\lambda_0=1\)；
\(\epsilon_j=\operatorname{sgn}j\)，\(\epsilon_0=0\)，\(\Pi=I-\Pi_0\)。
采用R43/R53的 \(E_{s,\rho}=(H^s_\rho)^2\)，权满足非负、递增、次可加。
负权按Hilbert完成及真正的反号权对偶解释。

给定有限实阶 \(s\)，取R53(53.2)的实际包络 \(\mathcal V\)，其中
\(p_s=2|s|+10\)。本篇的全部额外角指数均不超过该数。设
\[
 Q=\max(1,q,q^{-1},c,c^{-1}),\qquad
 M_\delta=256(1+\pi)Q^2\delta^{-3},\qquad N_\delta=1+M_\delta,
\]
\[
 J_s=2^{|s|+14}Q^2\mathcal V,\qquad
 T_s=2^{|s|+17}Q^4\delta^{-3}\mathcal V,
\]
\[
 \mathcal D_s=N_\delta^2T_s+(N_\delta^2+1)M_\delta J_s.
\tag{54.1}
\]
记R43的准确实符号和自伴ordering为
\[
 a_{\sigma\varepsilon}(\phi)=\frac1{2q}\int_0^\delta
 \frac{V(t,\phi-\sigma\varepsilon\tau(t))}{\sqrt t}\,dt,
 \qquad \tau(t)=\tfrac23t^{3/2},
\]
\[
 A_\sigma=\sum_{\varepsilon=\pm1}
 \Pi_\varepsilon D^{-1/2}M_{a_{\sigma\varepsilon}}
                   D^{-1/2}\Pi_\varepsilon,\qquad
 \mathcal B=i\,\operatorname{diag}(A_+,-A_-).
\tag{54.2}
\]
其中 \(D^{-1/2}e_0=0\)。这不删除真实均值；均值和所有跨号项在完整余项中。

**定理54.1。** R53的完整试解矩阵满足
\[
 \|W^{\rm app}(\delta)-I-\mathcal B:
             E_{s,\rho}\longrightarrow E_{s+2,\rho}\|
 \le\mathcal D_s.
\tag{54.3}
\]
因此同一个准确传播 \(\mathcal C(\delta,0)\) 满足
\[
 \boxed{\quad \mathcal C(\delta,0)Q_0=I+\mathcal B+\mathcal E_2,\qquad
 \|\mathcal E_2:E_{s,\rho}\to E_{s+2,\rho}\|
 \le\mathcal D_s+e^{\delta K_{s+2}}L_s(1+2\sqrt\delta+\delta).\quad}
\tag{54.4}
\]
\(K_{s+2},L_s\)正是R53的明确实际常数，不是额外未说明的存在性常数。
并且可以把 \(I+\mathcal B\) 换成准确普通酉及 \(J\)-酉的 \(e^{\mathcal B}\)，
只需再加
\[
 \tfrac12 e^{J_s}J_s^2
\tag{54.5}
\]
到(54.4)的余项界。\(J_s\)同时覆盖本证明使用的 \(s,s+1,s+2\) 窗口。

## 2. 先把试解写成准确物理矩阵

以下 \(B,C,B_\xi,C_\xi\) 都取在实际切面 \(\xi=\delta\)，乘法顺序按所写固定。
R53(53.10)及其完整径向导数给
\[
 \binom{U^{\rm app}}{\partial_\xi U^{\rm app}}
       =\mathscr T_\delta F_*(\delta),\qquad
 W^{\rm app}(\delta)=F_*(\delta)^{-1}\mathscr T_\delta F_*(\delta),
\]
\[
 \mathscr T_\delta-I=
 \begin{pmatrix}
 iM_C\epsilon\Gamma^{-1}&-M_B\Gamma^{-2}\Pi\\
 iM_{C_\xi}\epsilon\Gamma^{-1}+\delta M_B\Pi&
 iM_C\epsilon\Gamma^{-1}-M_{B_\xi}\Gamma^{-2}\Pi
 \end{pmatrix}.
\tag{54.6}
\]
这里使用自由非零列 \(p_\xi=-\delta\Gamma^2u\)；均值的 \(p_\xi=0\)，
所以准确的 \(\Pi\) 已经写入。特别，\(\mathscr T_\delta-I\) 的均值输入列为零。
不能把均值假装成 \(\lambda_0^2\delta\) 的振子后再做消去。

置 \(r=\sqrt\delta\)、\(t_0=1/(4\delta)\)。对所有 \(j\)，定义比较frame
\[
 G_\delta(j)=g_j
 \begin{pmatrix}1&1\\p_{j,+}&p_{j,-}\end{pmatrix},\qquad
 g_j=\frac c{\sqrt\pi}\delta^{-1/4}\lambda_j^{-1/2},\qquad
 p_{j,\sigma}=-t_0+i\sigma r\lambda_j.
\tag{54.7}
\]
它包含R46所需的真实 \(1/(4\delta)\) 振幅剪切，而不只含振荡相位。
准确有 \(\det G_\delta(j)=-2ic^2/\pi=\det F_*(\delta,j)\)，包括均值。

令 \(S=G_\delta^{-1}(\mathscr T_\delta-I)G_\delta\)。
对 \(j\ne0\)、任意输出 \(k\)，令 \(l=k-j\)。直接乘两个二乘二矩阵得到
\[
\begin{aligned}
 S_{\sigma\tau;kj}={}&
 \mathbf1_{\sigma=\tau}\,
 \frac{i(\epsilon_j C_l-\sigma rB_l)}{\sqrt{\lambda_k\lambda_j}}\\
 &+\frac{i(\epsilon_jC_l-\tau rB_l)}{2\sqrt{\lambda_k\lambda_j}}
                         \left(\frac{\lambda_k}{\lambda_j}-1\right)\\
 &+\frac1{2i\sigma r\sqrt{\lambda_k\lambda_j}}
 \left[
 \frac{i\epsilon_j(C_\xi)_l}{\lambda_j}
 +\frac{t_0(B_\xi)_l}{\lambda_j^2}
 -\frac{i\tau r(B_\xi)_l}{\lambda_j}
 +\frac{t_0^2 B_l}{\lambda_j^2}
 +\frac{i t_0r(\sigma\lambda_k-\tau\lambda_j)B_l}{\lambda_j^2}
 \right].
\end{aligned}\tag{54.8}
\]
对 \(j=0\) 则 \(S_{\sigma\tau;k0}=0\)。这给完整矩阵，而非单输入列的形式渐近。

为了核对(54.8)，第一物理槽的单列是
\[
 i\epsilon_jC_l/\lambda_j-B_l p_{j,\tau}/\lambda_j^2,
\]
第二槽是
\[
 i\epsilon_j(C_\xi)_l/\lambda_j+\delta B_l+
 (i\epsilon_jC_l/\lambda_j-(B_\xi)_l/\lambda_j^2)p_{j,\tau}.
\]
将第二槽减去 \(p_{k,-\sigma}\) 倍第一槽，再乘
\(\sqrt{\lambda_k/\lambda_j}/(2i\sigma r\lambda_k)\)，即得上式。
尤其两个幅度支之间原来可能的一阶项准确消失；剩余仍真实保留。

## 3. 所有频率块的二阶界

定义准确反自伴的同锥主项
\[
 \mathfrak B_\delta=
 i\,\operatorname{diag}\left(
 \sum_\varepsilon\Pi_\varepsilon\Gamma^{-1/2}
        M_{\varepsilon C-rB}\Gamma^{-1/2}\Pi_\varepsilon,\quad
 \sum_\varepsilon\Pi_\varepsilon\Gamma^{-1/2}
        M_{\varepsilon C+rB}\Gamma^{-1/2}\Pi_\varepsilon
 \right).
\tag{54.9}
\]
其 \(\Gamma^{-1/2}\) 在投影内使用，不涉及均值定义的歧义。
记
\[
 b_l=|B_l|+|C_l|+|(B_\xi)_l|+|(C_\xi)_l|,
 \quad
 U_p=\sum_l(1+|l|)^p e^{|\rho|\omega(|l|)}b_l.
\]
由R53(53.8)，只要 \(p\le p_s\)，就有 \(U_p\le32\mathcal V\)。

对所有 \(j\ne0\) 及 \(k\)，有
\[
 \frac{\langle k\rangle}{\sqrt2Q}\le\lambda_k\le Q\langle k\rangle,
 \qquad |\lambda_k-\lambda_j|\le Q(1+|k-j|),
\]
\[
 \frac{\lambda_k}{\lambda_j}\le1+Q^2(1+|k-j|).
\tag{54.10}
\]
当 \(k,j\ne0\) 时第一个差还可用 \(q|k-j|\)。若 \(k,j\) 异号，
\(|k-j|\ge|j|\)；若 \(k=0\)，也有 \(|k-j|=|j|\)。
所以(54.8)第一行在(54.9)没有保留的每一项，都可用一个lag因子再换取
一个输入频率的逆幂。这样，mean输出行与异号角频块都被计费。

逐项使用(54.10)、\(r=\sqrt\delta\)、\(t_0=1/(4\delta)\)、
\(\lambda_j^{-1}\le Q\) 可得共同的安全界
\[
 |(S-\mathfrak B_\delta)_{\sigma\tau;kj}|
 \le 8Q^2\delta^{-3}(1+|k-j|)b_{k-j}
                         \lambda_k^{-1/2}\lambda_j^{-3/2}.
\tag{54.11}
\]
其均值输入列为零。这里没有使用正负角频之间的距离作为未解释的
“任意平滑”：实际付出的仅是显示的一个lag因子，足够本篇二阶结论。

例如(54.8)的第二行付 \(Q(1+|l|)/2\)；
\(C_\xi,B_\xi\) 两类的系数分别付 \(1/(2r)\)、
\(1/2+t_0Q/(2r)\)；\(t_0^2 B\) 付 \(t_0^2Q/(2r)\)。
最后一类付
\[
 \frac{t_0}{2}\left(2+Q^2(1+|l|)\right).
\]
连同第一行被丢出同锥的真实项，这些费用之和小于(54.11)。

输入、输出加权之后，
\[
 \frac{\langle k\rangle^{s+2}}{\langle j\rangle^s}
       \lambda_k^{-1/2}\lambda_j^{-3/2}
 \le2Q^2\,2^{|s+3/2|/2}\langle k-j\rangle^{|s+3/2|}.
\tag{54.12}
\]
权比再付 \(e^{|\rho|\omega(|k-j|)}\)。对固定lag用平移的
\(\ell^2\) 等距，再作离散Young；两幅度支付因子2，得到
\[
 \|S-\mathfrak B_\delta:E_{s,\rho}\to E_{s+2,\rho}\|
 \le 2^{|s|+12}Q^4\delta^{-3}U_{|s|+4}\le T_s.
\tag{54.13}
\]
这证明完整强余项，不用逐列范数的不可求和累加。
同样对(54.9)直接用
\(\lambda_k^{-1/2}\lambda_j^{-1/2}\)，得到
\[
 \|\mathfrak B_\delta:E_{t,\rho}\to E_{t+1,\rho}\|\le J_s,
 \qquad t=s,s+1,s+2.
\tag{54.14}
\]
这些指数所需的 \(U_{|t|+1}\) 均由 \(p_s=2|s|+10\) 支付。

## 4. 准确Airy frame与比较frame之差有一阶增益

定义频率对角的二乘二乘子
\[
 A_\delta(j)=G_\delta(j)^{-1}F_*(\delta,j),\qquad
 E_\delta(j)=\operatorname{diag}_{\sigma=\pm1}
    e^{i\sigma(\lambda_j\tau(\delta)+\pi/4)}\quad(j\ne0),
\]
而 \(E_\delta(0)=I\)。本节证明
\[
 \|A_\delta-E_\delta:E_{t,\rho}\to E_{t+1,\rho}\|\le M_\delta
 \quad\hbox{对每个实数 }t,
\tag{54.15}
\]
\[
 \|A_\delta\|_{E_{t,\rho}},\ \|A_\delta^{-1}\|_{E_{t,\rho}}\le N_\delta,
 \qquad
 \|A_\delta^{-1}-E_\delta^{-1}:E_{t,\rho}\to E_{t+1,\rho}\|
 \le N_\delta M_\delta.
\tag{54.16}
\]
因为这些是频率对角矩阵，界与 \(t,\rho\) 无关；不能将其与非径向乘法混同。

对非零 \(j\)，置 \(t_j=\delta\lambda_j^{2/3}\)、
\(\eta_j=2t_j^{3/2}/3\)、\(Z_\tau=t_j^{1/4}Y_\tau(-t_j)\)。
准确有
\[
 (A_\delta)_{\sigma\tau}
       =\frac{\sqrt\pi}{2}\left(Z_\tau+
                       \frac{1}{i\sigma}\frac{dZ_\tau}{d\eta}\right).
\tag{54.17}
\]
R46的终端Volterra余项在 \(\eta\ge1\) 给
\[
 |Z_\tau-\pi^{-1/2}e^{i\tau(\eta+\pi/4)}|,
 \quad
 |Z_\tau'-i\tau\pi^{-1/2}e^{i\tau(\eta+\pi/4)}|
 \le\frac1{\sqrt\pi\,\eta}.
\tag{54.18}
\]
这里包括其明确的 \(5/(72\eta)\) 校正和 \(1/(4\eta^2)\) 误差，
故不从一个未定余项的渐近式推断全区间界。
于是 \(\|A_\delta(j)-E_\delta(j)\|\le2/\eta_j\)，乘
\(\langle j\rangle\) 后至多 \(3\sqrt2/(q\delta^{3/2})\)。

若 \(\eta_j<1\)，仍用R39的实际全轴界。由链式微分，
\[
 |Z_\tau|\le10,\qquad
 |Z_\tau'|\le\tfrac52t_j^{-5/4}+10t_j^{-1/4}+10.
\]
因为 \(t_j\ge\delta q^{2/3}\)、\(\langle j\rangle<3/(q\delta^{3/2})\)，
得到
\[
 \langle j\rangle\|A_\delta(j)-E_\delta(j)\|
 \le102\sqrt\pi\,Q^2\delta^{-11/4}\le M_\delta.
\tag{54.19}
\]
均值必须直接使用
\[
 F_*(\delta,0)=c
 \begin{pmatrix}1+i\delta/\pi&1-i\delta/\pi\\i/\pi&-i/\pi\end{pmatrix}.
\]
代入(54.7)可得 \(\|A_\delta(0)-I\|\le5\sqrt\pi\,\delta^{-5/4}\)，
同样小于 \(M_\delta\)。所以(54.15)覆盖全部频率。

由两个准确Wronskian，\(\det A_\delta(j)=1\)。二乘二矩阵的两个奇异值乘积
为1，因此 \(\|A_\delta(j)^{-1}\|=\|A_\delta(j)\|\)；结合(54.15)得到
前两个(54.16)界。最后使用准确恒等式
\[
 A_\delta^{-1}-E_\delta^{-1}
       =-A_\delta^{-1}(A_\delta-E_\delta)E_\delta^{-1}.
\]
没有要求 \(A_\delta-E_\delta\) 的同档norm小于1，也没有漏掉任何低频逆。

## 5. 恢复同一个射线积分和自伴ordering

准确有
\[
 W^{\rm app}=I+A_\delta^{-1}S A_\delta.
\]
由(54.13)–(54.16)，
\[
\begin{aligned}
 A_\delta^{-1}S A_\delta-E_\delta^{-1}\mathfrak B_\delta E_\delta
 ={}&A_\delta^{-1}(S-\mathfrak B_\delta)A_\delta\\
 &+(A_\delta^{-1}-E_\delta^{-1})\mathfrak B_\delta A_\delta\\
 &+E_\delta^{-1}\mathfrak B_\delta(A_\delta-E_\delta).
\end{aligned}\tag{54.20}
\]
第一行的二阶norm至多 \(N_\delta^2T_s\)，后两行分别至多
\(N_\delta^2M_\delta J_s\)、\(M_\delta J_s\)。这就是(54.1)。

还须准确辨认主项，不能只比较角平均。对同号 \(k,j\)、符号 \(\varepsilon\)，
两侧 \(E_\delta\) 的相位相乘为
\[
 e^{i\sigma(\lambda_j-\lambda_k)\tau(\delta)}
       =e^{-i\sigma\varepsilon q(k-j)\tau(\delta)}.
\]
R53(53.38)准确给
\[
 (\varepsilon C-\sigma\sqrt\delta B)(\phi)
 =\frac{\sigma}{2}\int_0^\delta
 \frac{V(t,\phi+\sigma\varepsilon[\tau(\delta)-\tau(t)])}{\sqrt t}\,dt.
\]
将 \(\phi\) 平移 \(-\sigma\varepsilon\tau(\delta)\)，并用
\(\Gamma^{-1/2}=q^{-1/2}D^{-1/2}\)，得到准确算子恒等式
\[
 E_\delta^{-1}\mathfrak B_\delta E_\delta
       =i\,\operatorname{diag}(A_+,-A_-)=\mathcal B.
\tag{54.21}
\]
因而(54.20)证明(54.3)。R53(53.22)随即给(54.4)。
对指数余项使用
\[
 e^{\mathcal B}-I-\mathcal B
       =\int_0^1(1-t)e^{t\mathcal B}\mathcal B^2dt
\]
及(54.14)，得到(54.5)。均值与跨锥都在已经支付的完整矩阵中；
指数主项在均值上为恒等，真实传播的均值仍由 \(\mathcal E_2\) 携带。

## 6. 与真实帽、完整反馈及源的衔接范围

本篇的输入根frame准确为 \(\mathscr S_0F_*(0)\)，与R53正侧完全一致。
若同一个正组件已经支付R53(53.25)的实际有限jet、R45/R47真实物理
Poisson/source/contact和边界变换，则其反射为
\[
 R_{\rm cap}^{S}=-I+\mathcal R_2.
\]
把这个反射与(54.4)接合，不需要再插入一个未校正根frame的4/3阶余项。
R46的strict区双槽传播、准确flux变角与fixed-cut Airy展开均为二阶强余项；
真实有限Sobolev变角有界，故有限次组合和已有准确有界消元保留二阶增益。
所需中间窗口、每个消元逆及所有交叉/均值槽，仍必须由实际网络输入提供。

特别，在R46所列的同一个双根反馈实现、真实正帽及普通有限Sobolev输入全部
成立时，其中“首相位加4/3余项”的余项可提升到二阶。首符号仍是同一个
R46/R50有限部密度；本篇没有产生另一个可自由选取的 \(\beta\)，共同剪切
也不改变 \(1/j\) 系数。

直接log权的负侧结论(54.4)不损宽度。正帽的非零权Robin/contact仍要按
R35/R53单独支付；strict传播和真实变角若共支付 \(\eta\) 阶损失，则完整
余项相应是 \(2-\eta\) 阶，不能仍写无损二阶。
在确已得到常首相位高频分母 \(c/|j|\) 且真实余项norm为 \(K\) 后，
高频Neumann门因此可以取
\[
 (K/c)\,N^{-(1-\eta)}<1,\qquad 0\le\eta<1.
\tag{54.22}
\]
这是输入齐备后的门，不是本候选已经通过的数值判断；全部低块和规范条件
仍需准确处理。

外部普通源始终为R53(53.23)的真实Duhamel项，正侧也始终使用完整接触
\(K=-H^*\) 及真实边界迹。相位首项仅描述齐次传播，不能支付一个被省略的源。
本课题仍须实际共轭、\(\beta\)区间、所有有限系数/正帽/低频输入、残差因子
Newton和固定握持的有限幅精确闭族；本篇没有降低README的完成标准。
