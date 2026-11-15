# R841 原 CM 点及指定下降点的准确表达式实际完成

日期：2026-11-15。状态：**原 \(\beta_C=f_4(c_1)\) 与原 \(f_R(c_1)\) 的准确表达式已取得；展开坐标、抽象 \(A\) 中的原像、\(\eta\) 和高度未取得。**

本结果消费 [R840](R840-certified-original-implicit-CM-value-and-first-jet.md) 的准确四响应及 [R791](R791-certified-original-Hom-descent-and-eta-inputs.md) 的原切向值；应用既有 (791R.16)、[R792](R792-original-beta-composition-and-Galois-cube-root.md) 的共轭方向与三同源公式。这里登记实际完成的消费者和准确原点，不把已有恢复公式重新编号为新定理。

## 1. 实际执行与准确对象

公开 [run 43774984563](https://github.com/Rogerhu12/math-research-public/actions/runs/43774984563)，compute job 132999220068，source commit
cbcaa616926e9d4cb7d1376d687c174df086da4b。

核心完成时间为2026-11-15 23:28:49 UTC；数学消费者实际0.037801001秒，core回执0.038300970秒，exit0、error为null。此次只构造来源绑定的准确算术表达式，不重新执行 CM 迹、Hom、原关系提升、取根搜索或 Norm。

实际4个完成阶段为来源、分母非零证明、原点程序、后继来源与零判义务。原点程序共有50个按内容散列标识的节点，格式为 original-L-arithmetic-DAG-v1。其中未知关系向量由**同一个原2420阶单位方阵的准确解**定义；没有把518位模向量当作准确坐标。

| 范围 | 实际状态 |
|---|---|
| 原 \(\beta_C=f_4(c_1)\) 的准确表达式 | true |
| 原 \(f_R(c_1)\) 的准确表达式 | true |
| 原点位于无穷远 | false |
| 展开后的数域坐标准确认证 | false |
| 旧 R792 展开坐标入口完成 | false |
| 抽象 \(A\) 中原坐标前像恢复 | false |
| \(\eta\) 或高度已算 | false |
| 新 CM、Hom、取根或 Norm 运算 | false |

原映射仍为次数1206的 \(f_4\)，以 \(f_4(c_0)=O\) 归一化；原 \(c_1=4424\)，局部参数 \(z=a-1\)。没有以任意逆同源原像替换原点。

## 2. 四个叶子的准确含义

令 \(\xi=M^{-1}r\) 为 [原 unit-chart](../notes/R787-original-unit-chart-exact-expressions-and-CM-value-consumer.md) 中固定 free1186、其余27个自由值为零的准确解。原 CM 值行及首jet行均已准确构成。程序的四个响应叶子是

\[
A_j=\ell_{A_j}\xi,\qquad
B_j=c_{B_j}+\ell_{B_j}\xi,\qquad j=0,1.
\tag{841.1}
\]

它们绑定原1234个五次基值/jet、准确 \(e_jZ\)、原选行/选列和原 Laurent 算子的来源。原 \(Z\) 的主元行负号、\(\kappa\)、\(246\)、一次 \(82^{10}\) 以及 \(c_0,c_1\) 相位不变。

原 R791 的 \(h_0=f_4^*(dx/(2y))/dz(c_1)\) 从真实 index4 读取，准确非零；不再施加第二次 \(c_1\) slash 或相位。原点程序另绑定原字段 \(b,\zeta\)，\(s=1+2\zeta\)。

这四个叶子允许后继选择准确数域后端，或在有效地方评价其模像。若后继要展开 \(M\) 或作准确零证，仍须恢复原大 \(F\) 行及 \(R_m,\kappa\) 文件；一个SHA引用不等于这些机器输入已经取回。

## 3. 所有逆节点的非零依据

定义

\[
Q=A_0^2-bB_0^2,\qquad
N=A_1B_0-A_0B_1.
\tag{841.2}
\]

R840的原地方给 \(B_0\) 的全部十四分支为单位，故特征零 \(B_0\ne0\)。因此实际原点有限，且 \(y_0=A_0/B_0\)。

由 R792(792.7)，在指定实嵌入下 \(b>0\)、\(y_0=s v_0\)，其中 \(v_0\) 属于固定实方向。因此

\[
y_0^2-b=-3v_0^2-b<0,\qquad Q\ne0.
\tag{841.3}
\]

这只使用指定嵌入，不声称所有嵌入都是实的。

原曲线的准确正则微分恒等式

\[
dy=3x^2\omega,\qquad \omega=\frac{dx}{2y}
\]

也在 \(y=0\) 处成立。故 \(x_0^3=y_0^2-b\ne0\) 与 \(h_0\ne0\) 给 \(y'_0=3x_0^2h_0\ne0\)，再由商微分

\[
N=B_0^2y'_0\ne0.
\tag{841.4}
\]

实际出现的 \(B_0^{-1},Q^{-1},N^{-1},s^{-1}\) 因而均带明确来源或证明。这里认证的是特征零非零；没有把 \(Q,N\) 自动称为辅助素点或原素数41处的单位。

## 4. 原点和原三同源像

应用原 (791R.16)，实际准确点为

\[
\boxed{\quad
\beta_C=f_4(c_1)=
\left(\frac{3h_0Q}{N},\frac{A_0}{B_0}\right).
\quad}
\tag{841.5}
\]

等式 \(N^3=27h_0^3Q^2B_0^2\) 来自同一个准确原映射的曲线及微分恒等式，不靠有限精度乘回升级。因而 (841.5) 是准确原点，不只是满足某些模关系的候选点。

令原 \(\alpha_3=1-\zeta^2\)，则 \(\alpha_3^3=3s\)。原指定同源 \([\alpha_3]\) 的像为

\[
\boxed{
\begin{aligned}
x_R&=-\frac{\zeta h_0(A_0^2+3bB_0^2)}{N},\\
y_R&=\frac{A_0(A_0^2-9bB_0^2)}{3sB_0Q}.
\end{aligned}}
\tag{841.6}
\]

程序把 (841.5)、(841.6)、原 \(y'_0=N/B_0^2\) 及唯一 \(F_b\) 根 \(u_0=\zeta x_0\) 都作为明确根节点。没有执行二十一次 Norm/因式分解，也没有从抽象同源的多值逆像中任选一点。

原下降及极化标度仍来自 R791：

\[
\kappa v^\dagger v
=3870+711s_1-801s_2-360s_3+612s_4+864s_5.
\tag{841.7}
\]

不得把它置为1。原 primitive 模型点仍按
\(q_R[c_1-c_0]=v\beta\) 解释，保真实 Weil 分量和全部原 Galois 运输。

## 5. 实际文件、配置与输入保留

| 文件 | bytes | SHA-256 |
|---|---:|---|
| p41-original-CM-response-beta-DAG-certificate.json | 4338 | 52b80ce26c5bb3c2f2aef6287255f879f747f476827d014aa7c6c47cca6cc51c |
| full-outputs-manifest.json | 1780 | de6b334f91db6ca6338127168dc608ee3e5590d2398e8177013987b4804e8b8f |
| full-outputs-manifest-reference.json | 186 | a5f6ac3918b76e7349a866d9e4d0b55fc5baea3aa60b581911ff2437d88bd1f1 |
| 原点程序 | 7239 | acaf1a1eea1346461c267209c236ae737b9f762cbfc794a9eaaf7c2ca93bbbb1 |
| 分母证明 | 2184 | 7d8110f9482a423ca7df31a79d5b78b96597f4ef42fad76518068de36f390fd8 |
| 后继接口 | 2415 | 0a44f05eb0126b44854d71f0a4f359cbb8eeaebadbb8784a2365c76ed2ae0ae4 |
| 来源阶段 | 2197 | e795fa0c2310ab8dfe5c4cbe0960df57bb3ddcf5c59819b324ae7b68094157f8 |
| R792-CM-DAG-stage-manifest-e8cb446a9f3927bbbf415e08.json.gz | 1957 | f9fa66e3ca60b6ee4fab49d8aeea110733c8363f81908497c9fae155f8374005 |
| R792-CM-DAG-retained-inputs.tar.gz | 1211692 | 1cc858ba3631209472b22211af1ffb0f1647b38db23aac2e57d5d97c67b45f7b |

完整配置 SHA-256：
58164ca82bd34771cf2d84e38be2f4e3991e8873ef46e597af690ba2fae27e6c。

核心 R792_original_CM_response_beta_DAG.py SHA-256
afb49c1ac4245674d29364789e817b566517e1f5bf6d506cee684ed03fa34b8b；
包装器 R792_public_original_CM_response_beta_DAG.py SHA-256
96045ab00c4b5f4a674031ddb7100b07af98ab5bd5b8560ab56665c0d8cdee66；
原消费证明 ce50b9c2d4a20c812c811a38ae40fa470f41f958adee018449f5ad676a8bcda3。

174个原输入恰为CM的165项和R791的9项；两组选件指纹分别为
86d551e90f18c12a1ae36cb4393444b5093f7f4b1d09db7fc3b23fb0436235a9、
aa9eed74a05bf79744e7c22505eed811679c1e16a52674ad7b2c5a000f61c1be。
原 CM 的89MB载体没有下载，旧 CM 值、切向、Galois矩阵及关系算术没有重算。

本次 active artifact 14185648917，名称
serre-global-R792-CM-response-beta-DAG-43774984563-1，
1320147 bytes，平台ZIP SHA-256
f848bab0e0d1b1e3ffdfd43c606687549d8dacc25d57316bb130340ae7d34d7f，
期限为2026-11-16 23:28:50 UTC。根实际纯IO下载了这个1.32MB完整ZIP并重哈希；14个成员、12项manifest及所选成员bytes/SHA、stage配置均与原输出一致，没有执行本地数学。机器节点、数值向量和回执只保于该一日artifact，未进入Git或Release。

## 6. 后继必须保留的准确零判边界

原 Galois 作用仍为

\[
T^j(x,y)=
\bigl(\rho_j^{-2}\sigma^j(x),\rho_j^{-3}\sigma^j(y)\bigr),
\qquad T^7=[\zeta^2].
\]

必须同时运输全部字段、原响应行与单位方阵；不能只运输有限精度的四个数。

后继点加法需要具体判定 \(O\)、\(x(P)-x(Q)\)、\(y(P)+y(Q)\)、\(y(P)\) 及所用图的分母。一次合法模非零可以证明特征零非零；模零不证明准确零。允许的准确零证来自实际 Hom 恒等式、已证原字段/共轭恒等式、准确 bordered determinant/rowspace 证书或已被准确接受的展开坐标。非零Hom不推出其在 \(c_1\) 取值非零。

本次并未执行这些点加法，也未把八节点高度结构化为已知数值。\(\eta\) 仍需原全局极除子和刚性化；高度仍需实际极化、分裂与周期输入。短候选的后继准确接受可按 [单值零证接口](../notes/R787-original-short-CM-candidate-exact-acceptance.md) 推进，但不是本次准确表达式成立的前提。

Serre主要目标仍OPEN。
