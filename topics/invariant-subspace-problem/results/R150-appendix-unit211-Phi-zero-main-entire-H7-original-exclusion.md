# Phi=0 主 rho 头零图：整个 H7 原权纤维排除

数据保存说明（2026-11-28）：可重算载荷已按根规矩8/15从main移除，相关旧链接只定位既有历史；当前保留生成源、参数定义、run与SHA，原数学及执行身份不变。


日期：2026-11-28（Asia/Taipei）  
会话：Astra-ISP-8542378f-20261127

## 1. 原范围与结论

本稿接 [H7 补图完整排除](R150-appendix-unit211-Phi-zero-main-rho-head-H7-complement-complete-exclusion.md) 后剩下的整条有限权纤维
$$
u=1+v,\qquad Q=1-v,\qquad \ell=1+2v,\qquad H_7(v)=0,
$$
$$
H_7(v)=48v^7+36v^6-12v^5+15v^4+42v^3-4v^2+2v+1.
$$
范围仍是原 unit211、LS、$\Phi=0$、物理 $D\ne0$ 的 distinct-singleton 图及其全部既有原单位。

本次完整 QQ 七维代数中的原返回等于一，排除 $H_7$ 的全部复权根及每个根上的全部原 $\lambda,T,z$ 值。没有在 $H_7=0$ 使用仅付补图的 P6/P9；没有选择一个 $v$ 根，也没有假设七次多项式不可约。

## 2. 用已经完成的 b=0 原覆盖支付原线性系数

一般第一二次头 $H_1=0$ 的原均值已有
$$
L=a(\lambda)T+b(\lambda)z+c(\lambda)=0,
\qquad z=Qt,
$$
其中 $a,b,c$ 的 $\lambda$ 次数分别为 $1,1,2$。完整精确系数来自已保存的原三均值 adjugate 行，不是任意加入的线性约束。

[一般 H1 中原 b=0 的 316 次覆盖](R150-appendix-unit211-Phi-zero-whole-first-head-linear-b-zero-316-weight-cover.md) 给出首一 QQ 多项式 $C_{316}(u)$：任何同一原 $H_1=0,b(\lambda)=0$ 解，连同该证明全部系数分母零纤维，都必须满足 $C_{316}(u)=0$。

本次只读取该已完成覆盖，不重复其原 F6 计算。令 $h_7=H_7/48$。实际在 QQ 上逐次乘回 $u=1+v$ 的 Horner 约化，并得到
$$
\gcd_{\mathbb Q[v]}\bigl(h_7(v),C_{316}(1+v)\bigr)=1.
$$
此外 $h_7$ 与其导数的 gcd 为一。因此整个 $H_7=0$ 原权纤维都避开了旧覆盖，准确支付
$$
b(\lambda)\ne0
$$
于本稿每个可能的原点。这里是已闭原零支带来的点值结论；没有把形式多项式 $b(\lambda)$ 当作整个多项式环的单位。

## 3. 整七维权代数与同一个原 L

所有新计算均在
$$
\mathcal A=\mathbb Q[v]/(h_7)
$$
的全部七维表示中完成。若需要对某个系数 $r\in\mathcal A$ 求逆，程序先对其 QQ 多项式代表与 $h_7$ 作真实 xgcd，再完整乘回；只有 gcd 为非零常数并且 $rr^{-1}=1$ 的全部七个坐标成立，才使用该逆。

程序实际对保存的 $L$ 系数作 $u=1+v,Q=1-v$ 特化，并用重新构造的完整原 $R_{\rm bar},W_4,O_{\rm bar}$ 核回
$$
L=\alpha_0R_{\rm bar}+\alpha_1W_4+\alpha_2O_{\rm bar},
$$
其中 $\alpha$ 正是原三个二次头矩阵 adjugate 的第零行。其头行列式在整 $\mathcal A$ 中为零。这个返回保留同一个原 $L$、同一个 $T,z,\lambda$；没有将单条原式的值谱系数擅自分别置零。

这一步在实际 0.048054 秒完成。全部所需权分母在整 $\mathcal A$ 上均取得真实逆，程序没有遇到非单位分支。它仍然把非单位时“保全整个未返回权因子”的退出路径写入源，未以默认域假设越过该问题。

## 4. 完整清 z 的三个原二次与固定四阶结果式

对任意一个原二次式，写成
$$
P=q_0+q_TT+q_zz+q_{TT}T^2+q_{Tz}Tz+q_{zz}z^2.
$$
系数是 $\mathcal A[\lambda]$ 中的多项式。定义
$$
\widetilde P=
(b^2q_0-bcq_z+c^2q_{zz})
$$
$$
\hspace{1.6em}
+\bigl(b^2q_T-b(aq_z+cq_{Tz})+2acq_{zz}\bigr)T
+\bigl(b^2q_{TT}-abq_{Tz}+a^2q_{zz}\bigr)T^2.
$$
实际逐项乘回完整原多项式恒等式
$$
b^2P-\widetilde P
=L\bigl(b(q_{Tz}T+q_z+2q_{zz}z)-q_{zz}L\bigr).
$$
所以每个原解使 $\widetilde P=0$。此式在任何值首项为零时也成立，不需要先倒置形式 $b$。

分别对原 $R_{\rm bar},W_4,N_1$ 得到
$$
R(T),\quad W(T),\quad N(T)\in\mathcal A[\lambda][T].
$$
三者的 $T$ 次数至多二，按 $T^0,T^1,T^2$ 排列的 $\lambda$ 次数均为 $(4,3,2)$。

对两个二次式
$$
p=a_2T^2+a_1T+a_0,\qquad
q=b_2T^2+b_1T+b_0
$$
使用固定原次数 $(2,2)$ 的四阶 Sylvester 行列式，其完整恒等式为
$$
\operatorname{Res}^{(2,2)}_T(p,q)
=(a_2b_0-a_0b_2)^2
-(a_2b_1-a_1b_2)(a_1b_0-a_0b_1).
$$
新源对该表达式与完整四阶行列式的全部七维系数实际核回。即使某个 $\lambda$ 值使 $T^2$ 首项退化，只要两个原式有共同有限 $T$，这个固定行列式仍为零；程序不在这些点改用降阶矩阵。

实际两个输入
$$
F_{12}=\operatorname{Res}^{(2,2)}_T(R,W),\qquad
G_{12}=\operatorname{Res}^{(2,2)}_T(R,N)
$$
的 $\lambda$ 次数均为 12。

## 5. 仅剥已付原 b 的四次幂，完整 QQ 返回一

$b$ 的 $\lambda$ 头系数在整 $\mathcal A$ 上取得真实逆。将它归一化为首一 $\widehat b$ 后，本次对两个十二次式分别作完整多项式短除及乘回，准确得到
$$
F_{12}=\widehat b^{\,4}F_8,\qquad
G_{12}=\widehat b^{\,4}G_8,
$$
其中 $F_8,G_8\in\mathcal A[\lambda]$ 的次数均为八。没有剥掉任何 $\lambda$ 因子，也没有倒置新的未知值因子。第二节已付 $b(\lambda)\ne0$，故每个原点必须满足
$$
F_8(\lambda)=G_8(\lambda)=0.
$$

随后完全在 $\mathcal A[\lambda]$ 中作 QQ 欧氏返回。实际余式次数依次为
$$
7,6,5,4,3,2,1,0,-1.
$$
每一步的除式头都在整七维代数上取得真实逆，每个商、除式、余式都完整乘回。最后规范化得到常数一。

因此由这些实际除法恒等式的逆向复合，存在
$$
U,V\in\mathcal A[\lambda]
\quad\text{使}\quad
UF_8+VG_8=1.
$$
该结论适用于 $\mathcal A$ 的全部复根嵌入；不需要把 $\mathcal A$ 擅自视为域，也不要求事先选择某个实根或复根。任意本稿原点的求值都会使左侧为零、右侧为一，矛盾。

源在这里已经完成整 $H_7$ 排除，随后预备的第三对结果式、全图 C71 和 D 目标分支均未执行。不得把未执行分支计入本次证据。

## 6. 实际执行与小参数

新自含源：

[2026-11-27-unit211-Phi-zero-main-entire-H7-original-linear-finite-weight-input-8542.py](../notes/2026-11-27-unit211-Phi-zero-main-entire-H7-original-linear-finite-weight-input-8542.py)

- Git blob：19cb09b0beb197eaa27c7e7b2913e890f44b5da5。
- SHA256：39a391bc8c2d2b28e31c78bcda62ed12f16048c407b222a15a62407a9adcbf5b。
- 实际 run/job：46057406228 / 140703149299。
- source commit：749287604b499044d844f73dc80208fe4f119581。
- 内层退出码 0；0.385492544 秒；峰值子进程 RSS 38508 KiB。
- stdout：7366 字节；SHA256 ae5a143fceab2726923fb09df0c0842900236127a632f464583b34b062b97f36。
- 实际完整七维逆 21 个、权关系约化乘回 20094 次、原 $\lambda$ 除法乘回 20 次。
- 全部原除法轨迹 SHA256：8d82967b342a7f76df2182cc24f9127cf9113b30a09d4dd11640b17ad5f78fd4。
- 2026-11-27 19:32:39 UTC 实际规则读取的两份 README blob 均无变化。

[小执行回执](../notes/2026-11-27-unit211-Phi-zero-main-entire-H7-original-exclusion-execution-8542.json) 保全部阶段、真实退出和执行身份。

[整七维原线性关系及最终约束的小精确参数](https://github.com/Rogerhu12/math-research-public/blob/3b9cda56dfa6a1ae9d4ca2a35fa81798a5f156c9/topics/invariant-subspace-problem/notes/2026-11-27-unit211-Phi-zero-main-entire-H7-original-exclusion-exact-input-8542.json) 解压后为 1013 字节，SHA256 ee007d42bae0c2d240929b81972714ecc61e7cc7cb3d174aee71256408bcf9a6。原完整 L 与 316 覆盖直接引用既有固定载荷，没有重放它们的旧推导。

本定理只关闭主 rho 头零图中的整个 $H_7$ 纤维。它与已闭补图合并后关闭该主图；一般第一二次头 $H_1=0$ 的其余权点、rho 二次头非零的 $\Phi=0$ 图以及原 $D=0$ 碰撞范围均不能由本定理直接外推。
