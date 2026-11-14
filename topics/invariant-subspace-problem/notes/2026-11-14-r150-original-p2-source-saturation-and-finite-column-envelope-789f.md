# R150：自然图之外的完整 \(p^2\) 来源饱和与有限列接口

日期：2026-11-14。作者：Astra-ISP-789f / literature_audit；
AI-assisted，GPT-6 Astra Pro。状态：以下为原有限模上的完整代数归约；
没有执行新的原式乘积、第三像或饱和计算。

本稿接
[低初值整数格](2026-11-14-r150-low-initial-integer-lattice-third-layer-and-five-relations-789f.md)
与[双倍 jet 第三层](2026-11-14-r150-third-bockstein-double-jet-smith-loss-and-local-source-789f.md)。
它说明：即使当前自然图中的全部 197 个原高核方向加五个关系方向给出否定，
还有哪一个准确的原整数来源商没有支付，以及如何用有限真实来源列构造它。
不改变固定原矩阵、目标、异常集或特征零完成标准。

## 1. 原整数余模与已经支付的自然来源

记 \(p=31\)、\(D=\mathbf Z_{(31)}\)、\(R_D=D[s]\)、\(R=\mathbf F_{31}[s]\)，
\[
 E=R_D^{6188},\qquad V=R_D^{4367},\qquad
 A:E\longrightarrow V,\qquad \mathcal C=\operatorname{coker}_{R_D} A.
\]
这里 \(\mathcal C\) 是**原整数余模**，不是已算的模 \(p\) 余模 \(Q\)，
也不是它的 315 维 torsion 块。

保存的来源为
\[
 b_i=A\kappa_i/p^{e_i},\qquad
 (e_1,\ldots,e_9)=(1,1,2,2,2,2,2,3,4).
\]
低初值稿已经精确证明自然图的原来源像为
\[
 H_{\rm nat}
 =p^2E+p\kappa_1R_D+p\kappa_2R_D
     +\sum_{i=3}^{9}\kappa_iR_D.
\tag{1.1}
\]
令
\[
 S_k=\{x\in E:Ax\in p^kV\},\qquad k\ge0.
\tag{1.2}
\]
显然 \(H_{\rm nat}\subset S_2\)。定义整数余模中的子模
\[
 B_{\rm nat}
 =R_D\langle[b_1],\ldots,[b_7],[p b_8],[p^2 b_9]\rangle
 \subset\mathcal C[p^2].
\tag{1.3}
\]
方括号表示模 \(\operatorname{im}A\) 的类，且
\(\mathcal C[p^k]=\{c:p^kc=0\}\)。

## 2. 完整来源缺口的精确商

定义
\[
 \phi_2:S_2\to\mathcal C[p^2],\qquad
 \phi_2(x)=[Ax/p^2].
\tag{2.1}
\]
因为 \(V\) 无 \(p\) 扭元，除式唯一。此映射满射：
若 \(c=[y]\in\mathcal C[p^2]\)，则 \(p^2y=Ax\) 对某个 \(x\in E\) 成立，
该 \(x\in S_2\) 且 \(\phi_2(x)=c\)。

其核准确为
\[
 \ker\phi_2=p^2E+\ker A.
\tag{2.2}
\]
确实，\([Ax/p^2]=0\) 当且仅当 \(Ax/p^2=Az\) 对某个 \(z\in E\) 成立，
即 \(x-p^2z\in\ker A\)。逐列计算 (1.1) 的像得到 (1.3)，所以
\[
 \boxed{
 S_2/(H_{\rm nat}+\ker A)
 \ \simeq\ \mathcal C[p^2]/B_{\rm nat}.
 }
\tag{2.3}
\]
这就是“是否每个有关原来源都可加一个真正原核后进入自然图”的准确对象。
只知道当前 \(F_9\) 模 \(p\) 的第一像或若干相关高阶像，不能把右侧写成零。

## 3. 原 \(p^6\) 精度的准确有限版本

当前固定原目标为 \(p^2h_0t\pmod{p^6}\)。在这一精度，
两个原来源有相同输出当且仅当其差属于 \(S_6\)。
因为 \(S_6\subset S_2\)，可以对上述同一映射计算
\[
 \boxed{\phi_2(S_6)=p^4\mathcal C[p^6].}
\tag{3.1}
\]

正向：若 \(x\in S_6\)，写 \(Ax=p^6y\)。则 \([y]\in\mathcal C[p^6]\)，
而 \(\phi_2(x)=p^4[y]\)。

反向：若 \(c=[y]\in\mathcal C[p^6]\)，取真正原来源 \(x\) 使
\(Ax=p^6y\)。则 \(x\in S_6\)，且 \(\phi_2(x)=p^4c\)。
这里没有把模 \(p\) 类的任意整数代表当成可整除的来源。

由 (2.2)，\(\ker\phi_2\subset H_{\rm nat}+S_6\)，故
\[
 \boxed{
 S_2/(H_{\rm nat}+S_6)
 \ \simeq\
 \mathcal C[p^2]/\bigl(B_{\rm nat}+p^4\mathcal C[p^6]\bigr).
 }
\tag{3.2}
\]
因此，若本稿右侧未证为零，图内的完整模 \(p^6\) 否定仍不能外推到
全部原整数来源。这个有限版本只比较来源覆盖，不会把必要的局部相容
变成原十七式的正证书。

## 4. 完整 \(S_2\) 的有限真实列构造

取原完整 \(\ker\bar A\) 的多项式基
\[
 K:R^h\longrightarrow R^{6188},\qquad h=1834.
\]
\(\widehat K\) 是它的固定原整数提升；令
\[
 R_1=A\widehat K/p\in\operatorname{Mat}(R_D).
\tag{4.1}
\]
定义第一 Bockstein 的完整源映射
\[
 \beta_1:R^h\to Q=\operatorname{coker}\bar A,\qquad
 c\mapsto[\overline{R_1}c],
\quad Z=\ker\beta_1.
\tag{4.2}
\]
必须求这个**源核** \(Z\)，不能仅保存 \(\operatorname{im}\beta_1\) 的像基。

选 \(Z\) 的任意有限多项式生成列 \(c_\ell\)，为每列取实际多项式解
\[
 \bar A q_\ell=-\overline{R_1}c_\ell.
\]
将 \(c_\ell,q_\ell\) 提升到原整数多项式，定义
\[
 \kappa(c_\ell)=\widehat K\,\widehat c_\ell+p\widehat q_\ell.
\tag{4.3}
\]
分子直接乘回表明 \(A\kappa(c_\ell)\in p^2V\)。

**完整生成公式为**
\[
 \boxed{
 S_2=p^2E+p\widehat K R_D^h
          +\sum_\ell\kappa(c_\ell)R_D.
 }
\tag{4.4}
\]

证明：首先
\[
 S_1=pE+\widehat K R_D^h
\]
由完整模 \(p\) 核基成立。给定 \(x\in S_2\)，写
\(x=pu+\widehat Kc\)。将 \(Ax/p=A u+R_1c\) 模 \(p\) 后，
有 \(\bar c\in Z\)。减去相应的 (4.3) 多项式组合后，
所得 \(x'\in S_2\) 被 \(p\) 整除，写成 \(p x_1\)。
由无 \(p\) 扭性得 \(x_1\in S_1\)，从而余项属于
\(p^2E+p\widehat K R_D^h\)。反向包含逐列显然。

不同允许整数提升或不同 \(q_\ell\) 不改变 (4.4) 生成的完整模；
但实际高阶除像仍须沿所选的固定代表计算，不能在后继 carry 中混用。

## 5. 用已成第一像构造 \(Z\)，而非重算旧第一层

本题实际第一像 \(\mathcal W=\operatorname{im}\beta_1\) 位于模 \(p\)
torsion，因此是有限维的 \(k=\mathbf F_{31}\) 空间。
取其已验证的基、实际 \(s\)-作用矩阵 \(J\)，以及全部原 \(h\) 个
第一像在该基中的常数坐标矩阵 \(C\)。
若 \(\mathcal W\) 的维数为 \(w\)，则
\[
 \mathcal W\simeq R^w/(sI-J)R^w.
\tag{5.1}
\]
为每个基向量选有**原核来源**的多项式提升，组成
\[
 T:R^w\to R^h,\qquad \beta_1(T e_j)=e_j\text{ 在 (5.1) 中}.
\]
此时 \(Z\) 的一组完整有限生成列为
\[
 \boxed{
 (I-TC)e_i\ (1\le i\le h),\qquad
 T(sI-J)e_j\ (1\le j\le w).
 }
\tag{5.2}
\]
所有列都在核中。反之，若 \(c\in Z\)，则
\(Cc=(sI-J)u\)，从而
\[
 c=(I-TC)c+T(sI-J)u.
\]
这证明完整性，不要求所列生成列线性无关，不把 \(s-2\) 当作单位，
也不引入未经支付的有理参数分母。

(5.2) 只需复用完整已成第一像、其真实 \(s\)-不变闭包和基的原来源。
后继仍要把 (4.3) 的实际 \(q_\ell\) 运输回原 \(6188\) 行。
可先按已保存的真正整数核与 \(H_{\rm nat}\) 消列，再只恢复仍可能非零的
组合；不能仅因某列的模 \(p\) 像为零而删掉它。

## 6. 旧 198 来源给出的具体未缩放入口

对旧第一像为零、已有同一完整第一校正 \(q_{1,j}\) 的来源，
直接令
\[
 \widetilde\kappa_j=\widehat K_j-p\widehat q_{1,j},\qquad
 \widetilde b_j=A\widetilde\kappa_j/p^2.
\tag{6.1}
\]
这是 (4.3) 的具体支路，确为原整数 \(S_2\) 来源。
当前 197 相关第三任务使用的原来源形如
\[
 p^2\widetilde\kappa_j-p^4\widehat q_{2,j}
       -\sum_{i\le7}p^{4-e_i}\kappa_i\widehat C_{ij},
\tag{6.2}
\]
其中 \(p^2\widetilde\kappa_j\) 已在 \(p^2E\subset H_{\rm nat}\) 中。
所以该第三任务完整完成，也没有自动覆盖 (6.1) **未乘 \(p^2\)**
的原来源进入位。

本稿没有断言每个 (6.1) 都给独立的新方向；它可能在真实
\(H_{\rm nat}+\ker A\) 或有限 \(H_{\rm nat}+S_6\) 商中为零。
应依 (4.4) 的完整来源商实际判断。旧精确整数 syzygy 可以删除，
旧第一/第二/第三“像张成”不能替代这种删除。

## 7. 一般递归与停止条件

更一般地，若 \(U_k\) 完整生成 \(S_k\)，且
\(AU_k=p^kV_k\)，取完整核基
\[
 K_k=\ker(\bar V_k)
\]
及整数提升，则
\[
 U_{k+1}=[pU_k,\ U_k\widehat K_k],\qquad
 V_{k+1}=[V_k,\ V_k\widehat K_k/p]
\tag{7.1}
\]
严格生成 \(S_{k+1}\)，并保每列的原来源。
证明与第 4 节相同；\(U_k\) 本身有关系也不影响生成论证。

一个必须保留的边界是：
\[
 \beta_1(F)=0\quad\text{不推出整数 }p\text{-饱和已稳定}.
\]
例如一列矩阵 \(F=[p^2]\) 的第一模 \(p\) Bockstein 像为零，
但第一次真正除列是 \(p\)，下一次是 \(1\)。因此，若追完整饱和，
需保实际除列或完整下一层来源，不能只凭当前第一像为零停机。

本稿没有计算 (2.3) 或 (3.2) 的实际维数，也不判定它是否为零；
没有开启新的数值任务。它给出的是当前自然图否定之后的精确有限来源
问题及可复用旧第一层数据的完整构造。
