# 全权一实际模函数的固定除法单位模型

日期：2026-11-12。状态：全部标签、周期归一、切向公式、整模型和
固定有限维 Kummer 输入均已证明。此处没有由 Kummer 类非零推断
临界 Bockstein 或 Sha 判据非零。

## 1. 固定 Legendre 家族与原来的全部标签

取
\[
E_\lambda:\ y^2=x(x-1)(x-\lambda),\qquad
\omega_\lambda=\frac{dx}{2y},\qquad D_\lambda=d/\omega_\lambda,
\]
并在 \(\lambda=1/2\) 处令 \(t=\lambda-1/2\)。
取固定全 \(N=68\) 级覆盖，使全部 \(E_\lambda[N]\) 分裂为带标签的
截面。原 [R47](../results/R47-central-borel-modular-form-and-exact-growth.md)
的同一组 \(256\) 个标签
\(\mathcal S=\{(r_P,s_P)\}\subset(N^{-1}\mathbb Z/\mathbb Z)^2\)
定义非零截面 \(P_\lambda\)；不随素数或权改变标签。

在复邻域选
\[
\omega_1(\lambda)=2\mathbf K(\lambda),\qquad
\omega_2(\lambda)=2i\mathbf K(1-\lambda),\qquad
\tau=\omega_2/\omega_1.
\tag{1}
\]
这里 \(\mathbf K\) 的输入是 Legendre 参数，不是其平方根。
\(\omega_1\) 是 \(\omega_\lambda\) 的周期；在 \(\lambda=1/2\) 有
\[
\omega_1=\sqrt2\,\Omega_0,\qquad
\omega_1(\lambda)=\pi_{\mathbb C}\vartheta_3(\tau)^2.
\tag{2}
\]
例如 (1) 可直接把 \(\int_1^\infty dx/(2y)\) 代入 \(x=v^{-2}\)
化成 \(\mathbf K(\lambda)\)，完整闭圈再乘 \(2\)。

定义带规范的非全纯修正
\[
U_P(\lambda)=
 \zeta_\lambda(r_P\omega_1+s_P\omega_2)
             -r_P\eta_1-s_P\eta_2,\qquad
S(t)=\sum_{P\in\mathcal S}U_P(1/2+t).
\tag{3}
\]
固定挠点标签使它实际全纯。本文下面给完全代数的公式。

## 2. 每一个 \(U_P\) 的准确除法函数公式

取 \(N\) 除法函数 \(\Psi_N\)，规范为
\[
\Psi_N(z)=\frac{\sigma_\lambda(Nz)}
                   {\sigma_\lambda(z)^{N^2}}.
\]
它是 \(E_\lambda\) 上的有理函数，满足
\[
\operatorname{div}\Psi_N
 =\sum_{Q\in E_\lambda[N]\setminus\{O\}}(Q)-(N^2-1)(O).
\tag{4}
\]
乘任何非零常数都不影响以下公式。
所有 \(P\ne O\) 都是简单零点，因此
\[
\boxed{\qquad
U_P=-\frac1{2N^2}
           \frac{D_\lambda^2\Psi_N(P)}
                {D_\lambda\Psi_N(P)}.
\qquad}
\tag{5}
\]

证明保留了常数项。令 \(NP=r\omega_1+s\omega_2\)，
局部参数 \(z\) 满足 \(dz=\omega_\lambda\)。
由 sigma 准周期，在 \(P+z\) 处
\[
D_\lambda\log\Psi_N(P+z)
 =N\zeta_\lambda(NP+Nz)-N^2\zeta_\lambda(P+z)
 =\frac1z-N^2U_P+O(z).
\]
另一方面，写
\(\Psi_N(P+z)=az+bz^2+\cdots\)，则同一个常数项是
\(b/a=D_\lambda^2\Psi_N(P)/(2D_\lambda\Psi_N(P))\)。
比较即得 (5)。这不是只由留数确定的等式。

因此 (3) 是固定全级覆盖上的一个显式代数函数：
只需整数除法函数 \(\Psi_{68}\) 及其沿不变微分的两个导数。
没有引入随 \(p\) 增长的除法多项式。

## 3. 与实际全权 \(M_1\) 的常数和角色

R47 的格缩放公式直接给
\[
\boxed{\qquad
\frac{\mathcal G(\tau)}
     {\pi_{\mathbb C}\vartheta_3(\tau)^2}
             =S(t).
\qquad}
\tag{6}
\]
确实，\(\mathcal G(\tau)=\omega_1\sum_PU_P\)，再用 (2)。
这里是 R47 的实际权一 \(\mathcal G\)，不是半权 \(F^2\)。

记 \(S_+(t)=(S(t)+S(-t))/2\)。
在[全权 GM 临界行](2026-11-12-full-weight-one-gm-critical-rows.md)
的规范中，准确有
\[
\boxed{\qquad
M_1(t)=c_*S_+(t),\qquad
 c_*=\frac{\sqrt2\,17^{17/4}}{4800f},
 \qquad f=34(1+i).
\qquad}
\tag{7}
\]
根取与正实周期相容的 \(\sqrt2\)、\(17^{1/4}\)。

核对 (7)：该笔记中
\(q_0=-8i17^{3/2}\)、
\(24e_4q_0^4=4800/17^4\)。
又
\[
\mathscr B(q_0u)=
  \frac{\pi_{\mathbb C}\vartheta_3(i)^2}{f\Omega_E}
                              K(t)S(t)
 =\frac{\sqrt2\,17^{1/4}}f K(t)S(t).
\]
取偶部分再除 \(24e_4q_0^4\)，正好得到 (7)。
因此所有常数均已固定，且 \(M_1=t^4+\cdots\) 是已证实际归一化。

偶部分同样可以用一组固定标签表示。
令
\(\mathcal S^{\rm rot}=\{(s,-r):(r,s)\in\mathcal S\}\)，
并置 \(S_{\rm rot}(t)=\sum_{\mathcal S^{\rm rot}}U_P(1/2+t)\)。
同源
\[
E_\lambda\longrightarrow E_{1-\lambda},\qquad
(x,y)\longmapsto(1-x,iy)
\]
把微分乘以 \(i\)，并把旧标签 \((r,s)\) 送到新标签 \((-s,r)\)。
因此
\[
S(-t)=-iS_{\rm rot}(t),\qquad
S_+(t)=\tfrac12(S(t)-iS_{\rm rot}(t)).
\tag{8}
\]
这明确保留了原始角色及偶投影，不能只把任意挠点和代入 (7)。

## 4. 所有目标素数处的整模型

在 \(\mathbb Z[1/(2N)]\) 上，于 \(\lambda=1/2\) 的正式邻域，
Legendre 曲线光滑，判别式 \(16\lambda^2(1-\lambda)^2\) 为单位。
有限覆盖 \(E[N]\) étale；选择原标签所在分支只需要一个有限
未分歧扩张，其完成环记为 \(\mathcal O\)。

若 \(p\nmid2N\)，全部非零 \(N\) 挠点约化后仍非零且互异。
标准整数除法函数 (4) 的首项系数 \(N\) 为单位；
其零除子在特殊纤维仍恰为这些简单点。
所以在每个相关挠点分支
\[
D_\lambda\Psi_N(P)\in\mathcal O[[t]]^\times.
\tag{9}
\]
这里 \(D_\lambda\) 是由整非消失微分 \(\omega_\lambda\) 对偶的整向量场。
因而 \(D_\lambda^2\Psi_N(P)\) 整，(5) 给
\[
U_P,\ S,\ S_{\rm rot},\ S_+\in\mathcal O[[t]]
                             \qquad(p\ne2,17).
\tag{10}
\]
(9) 使用的是全部非零 \(E[68]\) 的可分约化，
不是只验证某一数值样例的分母。

(7) 的 \(c_*\) 在 \(p\notin\{2,3,5,17\}\) 为单位。
\(M_1\) 已有有理 Taylor 系数，故与 \(\mathcal O\) 的整性相交，得到
\[
\boxed{\qquad
M_1\in\mathbb Z_p[[t]]
                 \quad\text{对每个 }p\notin\{2,3,5,17\}.
\qquad}
\tag{11}
\]
因此全权 GM 临界行笔记中的固定坏位集合可以明确取为
\(\{2,3,5,17\}\)，不再需要一个未经计算的额外判别式集合。

## 5. 真正固定的 relative Kummer 单位与切向值

令 \(t_E(Z)=-x(Z)/y(Z)\) 为沿纤维的正式参数；
它与模参数 \(t\) 不同。
它是奇函数且 \(t_E(z)=z+O(z^3)\)。
对每个非零 \(P\in E[N]\)，定义固定有理函数
\[
r_P(Z)=
 \frac{\Psi_N(P+Z)}
      {D_\lambda\Psi_N(P)\,t_E(Z)}.
\tag{12}
\]
在 \(Z=O\) 的零相消，准确有
\[
r_P(O)=1,\qquad
D_Z\log r_P(O)=-N^2U_P.
\tag{13}
\]
没有用一个只在复域定义的正则化代替 (12)。

\(t_E\) 的除子为
\((O)+(T_0)-(T_1)-(T_\lambda)\)。
因此 (12) 的全部零极点都在 \(E[N]\setminus\{O\}\) 上。
它是固定开族
\[
\mathcal U=E_\lambda\setminus(E_\lambda[N]\setminus\{O\})
\tag{14}
\]
上的真单位，并在 (9) 的全部好整模型上保持如此。

置
\[
R_{\mathcal S}=\prod_{P\in\mathcal S}r_P,\qquad
R_{\rm rot}=\prod_{P\in\mathcal S^{\rm rot}}r_P.
\]
则 (7)、(8)、(13) 给出实际切向公式
\[
\boxed{\quad
M_1(t)=-\frac{c_*}{2N^2}
 \left(D_Z\log R_{\mathcal S}(O)
          -iD_Z\log R_{\rm rot}(O)\right).
\quad}
\tag{15}
\]
这是两个固定 relative Kummer 单位的代数线性组合；
没有把未知的模函数误认成它们的普通 \(p\) 进对数。

## 6. 固定有限秩 GM 输入及尚需保留的精确项

开纤维 (14) 是 genus \(1\) 曲线删去 \(N^2-1\) 个点，
故其 relative de Rham 群有秩
\[
2+(N^2-1)-1=N^2=4624.
\tag{16}
\]
可由 residue 正合列直接得到：
\(H^1_{\rm dR}(E)\) 的秩为 \(2\)，剩下是这些点的
总和为零的 residue 空间。
此处存在真正的 integrable Gauss–Manin connection；
使用的是 Katz–Oda (1968), Theorem 1, p.204 的 smooth-family
relative de Rham 构造，不是此前多变量空间上的部分向量场连接。

每个 \([d_{\rm rel}\log r_P]\) 为 GM-horizontal：
绝对闭形式 \(d\log r_P\) 给出其闭提升；
等价地，沿任意局部基方向的 Lie 导数是一个相对全微分。
这些 Kummer 类给 residue 部分的全部秩 \(N^2-2\)。
确实，写
\[
D_N=\sum_{Q\in E[N]\setminus\{O\}}(Q)
                  -(T_0)+(T_1)+(T_\lambda),
\]
则
\[
\operatorname{div}r_P=D_N-N^2(-P).
\tag{17}
\]
两点相减的 residue 向量张成总和为零的全部空间。
同 residue 的代数线性组合关系已由有理关系张成；
清除整数分母后，相应单位乘积除子为零，故为常数，
其 \(d\log\) 也为零。因而这些类给一个显式的水平 Tate 部分，
并非只有维数计数的候选。

实际组合
\(\sum_{\mathcal S}[d\log r_P]-i\sum_{\mathcal S^{\rm rot}}[d\log r_P]\)
非零：在两组点和三个非零二挠点以外，(17) 的 residue 是
\(256(1-i)\ne0\)。这类点存在，因为全部非零点共有 \(4623\) 个，
两组标签合并至多有 \(512\) 个。

但 (15) 使用指定单位代表的一阶切向值。
Frobenius 在 cohomology 上比较 Kummer 类时会去掉一个相对全微分；
这个全微分在 \(O\) 的切向值通常不为零。
形式上，对于与标签相容的 Frobenius lift，
\[
d\log\varphi^*r^\sigma
 =p\,d\log r+
       d\log\left(\frac{\varphi^*r^\sigma}{r^p}\right).
\tag{18}
\]
右端最后一项在合适的刚性邻域可由 \(p\) 进对数写成全微分，
但不能据此在 (15) 或全权临界 residue 中删去它。
因此 (14)–(18) 提供了固定有限维 Kummer/GM 输入和明确的
切向代表；还缺将该精确 Frobenius 项与
\(C_{p+1}/p\)、\(C_{p-1}/p^2\) 对接并证明其无穷非零。

### 已核来源

- 实际 R47 的 \(256\) 标签、权一模形式及格缩放：
  [中央 Borel 原证明](2026-11-12-central-borel-modular-uniformization.md)。
  本文的除法函数及切向等式直接从同一个 sigma 规范推导。
- 全权临界系数、\(q_0\)、\(e_4\)：
  [全权 GM 临界行](2026-11-12-full-weight-one-gm-critical-rows.md)，
  及 R51 的准确平方常数。
- N. Katz, T. Oda (1968),
  *On the differentiation of de Rham cohomology classes with respect
  to parameters*, J. Math. Kyoto Univ. **8**, 199–213：
  §2、Theorem 1 (p.204)；
  [原文](https://www.its.caltech.edu/~matilde/GaussManinKatzOda.pdf)。
  原文已逐项核对；这里仅引用真正 relative de Rham 连接的存在与可积性。
