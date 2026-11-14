# R150：完整原 \(p^2\) 来源包缩为同一 197 个未缩放来源

日期：2026-11-14。作者：Astra-ISP-789f / literature_audit；
AI-assisted，GPT-6 Astra Pro。

状态：由本库已经证明的**完整源基**和已保存的实际四列 recipe 得出的
精确代数结论。没有重算旧第一像、四列第二像、197 第三像或任何原乘积。
本稿将[完整来源饱和接口](2026-11-14-r150-original-p2-source-saturation-and-finite-column-envelope-789f.md)
的原 \(S_2\) 包精确缩到 197 个已有来源类型；不把当前 197 第三任务
误报为这个扩大包的像问题已经解决。

## 1. 原模与本稿用到的真实基

沿用
\[
 p=31,\quad D=\mathbf Z_{(31)},\quad R_D=D[s],\quad R=\mathbf F_{31}[s],
\quad A:E=R_D^{6188}\to V=R_D^{4367},
\]
\[
 S_k=\{x\in E:Ax\in p^kV\},\qquad
 H_{\rm nat}=p^2E+p\kappa_1R_D+p\kappa_2R_D+\sum_{i=3}^{9}\kappa_iR_D.
\tag{1.1}
\]
\(H_{\rm nat}\subset S_2\) 已由原整数格定理支付。

[完整第一核稿](2026-11-14-r150-full-first-bockstein-kernel-and-second-interface-789f.md)
给 \(\ker\bar A\) 的全部 1834 个 \(R\) 基向量：
1632 个已有真正 \(D[s]\) 整数 syzygy 的低方向，和
\(K_1,\ldots,K_{202}\)。
令 \(K_{\rm low}\subset\ker A\) 为这些 1632 个固定真提升生成的模。

完整第一 Bockstein 映射记为
\[
 \beta:\ker\bar A\to Q=\operatorname{coker}\bar A.
\]
它在 \(K_1,\ldots,K_{198}\) 上为零，余下四列的像生成已验证的
二维 \(s\)-不变空间 \(W\)。实际第一除列 \(\kappa_1,\kappa_2\)
的像生成同一个 \(W\)；并不是仅在某个相关投影中生成。

令 \(\ell=(s-1)(s-2)\)。同稿在**原来源自由模**中证明
\[
 \begin{aligned}
 S_{200}&=K_{200}-(12s+10)K_{199},\\
 S_{201}&=K_{201}-(25s+21)K_{199},\\
 S_{202}&=K_{202}-(16s+21)K_{199},\\
 S_\ell&=\ell K_{199}.
 \end{aligned}
\tag{1.2}
\]
连同低 1632 方向和 \(K_1,\ldots,K_{198}\)，这四列构成
\(\ker\beta\) 的完整 \(R\) 基。其证明用源模的三角单位变换和
\(\operatorname{Ann}(\beta K_{199})=(\ell)\)，没有只数像的维数。

## 2. 四个实际 \(\kappa_3,\ldots,\kappa_6\) 确实提升这四个源基

[四列完整原式稿](2026-11-14-r150-four-genuine-second-bockstein-insufficiency-789f.md)
保存的 primitive 来源 `fourK2.bin` 的 SHA256 为
\[
\texttt{653867bccc606ec234c65eacfbb014fe14e055fcd50f2ea3f2506344d2aad8c7}.
\]
这是当前 \(\kappa_3,\ldots,\kappa_6\) 的四条固定来源，标签依次
4001、4002、4003、4004。

本稿还读取了其
[原 four runner](2026-11-14-r150-four-second-bockstein-runner-789f.py)：
`RELATIONS` 在原 \(K_{199},K_{200},K_{201},K_{202}\)
四行上的四列，逐列正是 (1.2)；原 recipe 进一步减去同次恢复的
\(p q_i\)，随后按 \(p^3\) 取 canonical 来源。
因此在完整 \(E/pE\) 中准确有
\[
 (\bar\kappa_3,\bar\kappa_4,\bar\kappa_5,\bar\kappa_6)
 =(S_{200},S_{201},S_{202},S_\ell).
\tag{2.1}
\]
canonical \(p^3\) carry 不改变此式，且已执行的原乘回保证
\(\kappa_3,\ldots,\kappa_6\in S_2\)。

这使用的是旧实际四列，未将后来
[成本 86 的单位改基](2026-11-14-r150-first-bockstein-kernel-cost86-appendix-789f.md)
误当作已经重跑的原来源。

## 3. 选取同一 197 个未缩放来源

对 \(j=2,\ldots,198\)，取旧已经选定的完整第一校正
\(\widehat q_{1,j}\)，使
\[
 \bar A q_{1,j}=A\widehat K_j/p\pmod p.
\]
定义真正的整数多项式来源
\[
 \widetilde\kappa_j=\widehat K_j-p\widehat q_{1,j}.
\tag{3.1}
\]
则
\[
 \widetilde\kappa_j\in S_2,\qquad
 \overline{\widetilde\kappa_j}=K_j.
\tag{3.2}
\]

[第七来源的精确稿](2026-11-14-r150-first-high-kernel-exact-seventh-source-and-197-reduction-789f.md)
由原 recipe 已证明
\[
 \bar\kappa_7=22K_1.
\tag{3.3}
\]
所以 \(\kappa_7/22\in H_{\rm nat}\subset S_2\) 可作为 \(K_1\) 的提升。
本稿只需要这条**源级单位初值**。不要求第七 recipe 的第一校正
与旧逐列 \(q_{1,1}\) 在整数中完全相同；该差不能靠略去 carry 消掉。

置
\[
 L=H_{\rm nat}+K_{\rm low}
          +\sum_{j=2}^{198}\widetilde\kappa_jR_D.
\tag{3.4}
\]
以上每列均在 \(S_2\)，故 \(L\subset S_2\)。
以下证明反向包含。

## 4. 完整包定理

\[
 \boxed{
 S_2=H_{\rm nat}+K_{\rm low}
             +\sum_{j=2}^{198}\widetilde\kappa_jD[s].
 }
\tag{4.1}
\]

这里 \(\bar L\) 表示 \(L\) 在 \(E/pE\) 中的像，不把它与抽象
\(L/pL\) 免费等同。

**第一步：\(\bar L=\ker\beta\)。**
一般第一提升定义给
\(\overline{S_2}=\ker\beta\)：一个 \(\bar A\)-核初值能提升到 \(S_2\)，
当且仅当它的第一 Bockstein 类为零。
(2.1)、(3.2)、(3.3) 以及 1632 个真低核，已经把
第 1 节的完整 \(\ker\beta\) 源基全部放入 \(\bar L\)。
因此 \(\bar L=\ker\beta\)。

**第二步：\(pS_1\subset L\)。**
由于完整 \(\beta\) 像由 \(\beta\bar\kappa_1,\beta\bar\kappa_2\) 生成，
每个 \(k\in\ker\bar A\) 都可写成
\[
 k=z+c_1\bar\kappa_1+c_2\bar\kappa_2,\qquad z\in\ker\beta,\quad c_i\in R.
\]
取 \(z\) 在 \(L\) 中的真正整数提升，其他系数任取整数多项式提升，
则对任何整数提升 \(\widehat k\)，有
\[
 \widehat k-z_D-c_{1,D}\kappa_1-c_{2,D}\kappa_2\in pE.
\]
乘 \(p\) 后，
\[
 p\widehat k\in pL+p\kappa_1R_D+p\kappa_2R_D+p^2E\subset L.
\tag{4.2}
\]
完整 \(\bar A\)-核基给 \(S_1=pE+\widehat K R_D^{1834}\)，
故 \(pS_1\subset L\)。

**第三步：任意 \(x\in S_2\) 均在 \(L\)。**
第一步允许选 \(l\in L\) 使 \(x-l=py\)。
两者的 \(A\) 像都被 \(p^2\) 整除，无 \(p\) 扭性给 \(y\in S_1\)。
第二步遂给 \(x=l+py\in L\)。反向包含已证，得到 (4.1)。

整个证明只作两次有限源级消去。不诉诸 \(p\)-进完备性，
不需要无限校正级数，也不把 \(p\) 当作 \(D[s]\) 的 Jacobson 根元来
套用不适用的 Nakayama 步骤。

不同合法 \(q_{1,j}\) 的选择之差乘 \(p\) 属于 \(pS_1\)，已由
第二步一起覆盖。故完整包结论与这种选择无关；具体高阶余量仍须使用
其固定代表和实际 carry。

## 5. 对应的完整整数像包

令
\[
 \widetilde b_j=A\widetilde\kappa_j/p^2,\qquad j=2,\ldots,198,
\]
并定义实际有限列矩阵
\[
 B_{\rm sat}=
 [A,\ b_1,\ldots,b_7,\ p b_8,\ p^2 b_9,\
          \widetilde b_2,\ldots,\widetilde b_{198}].
\tag{5.1}
\]
低核的 \(A\) 像严格为零。由 (4.1)，
\[
 \boxed{
 \operatorname{im}_{D[s]} B_{\rm sat}
 =(\operatorname{im}A:p^2)
 =\{v\in V:p^2v\in\operatorname{im}A\}.
 }
\tag{5.2}
\]
因此上一稿的图外来源商，确实由这 **197 个未缩放**来源生成；
不是仅给候选的若干新列。

对于原 \(p^2h_0t\pmod{p^6}\)，准确等价为
\[
 \boxed{
 \exists x\in E:\ Ax=p^2h_0t\pmod{p^6}
 \quad\Longleftrightarrow\quad
 \exists y:\ B_{\rm sat}y=h_0t\pmod{p^4}.
 }
\tag{5.3}
\]
左到右先由目标可除 \(p^2\) 得 \(x\in S_2\)，再用 (4.1)；
右到左按各列的真实来源乘回 \(p^2\)。
所有分母仅允许 \(D\) 的单位，且不增加原 \(m\)-单项式次数范围。

## 6. 与当前 197 第三任务的区别

当前第三任务使用
\[
 p^2\widetilde\kappa_j-p^4\widehat q_{2,j}
    -\sum_{i\le7}p^{4-e_i}\kappa_i\widehat C_{ij}
\]
来改变已付自然图的更高位。其局部相关像在当前商中的相容或不相容，
都不等于 (5.3) 已计算。

在 (5.1) 中，\(\widetilde b_j\) 是未缩放的整数列；
它们的初值、互相关系及以后 carry 都可以产生当前自然图没有覆盖的进入位。
要排除全部固定 \(p^2\) 原整数来源，须完成 (5.3) 的完整允许来源，
不能只重用这些列的某一个局部第三投影。
正解仍须恢复原 \(6188\) 行并核全十七式模 \(p^6\)。

(4.1) 没有给未知最小费用，也没有说 197 列线性独立。
任何有限参数预算或局部化算法都应另付实际次数、完整 free 条件、
所有必要 primary 及原来源运输。本稿不宣称特征零有理来源、
更高 \(m\) 次数来源或普通 Hilbert ISP 已解决。
