# R133 补篇：真实标量 mean 回填的连续响应与伴随体残差消费者

2026-11-14。本文把
[精确 mean 消元](R133-supplement-exact-mean-elimination-full-adjoint-and-nu-Schur.md)
实现为一个可检查的完整体区消费者。**源码已经完成，运行时失联，尚未执行。**
它不把未恢复的 trial 数组或原失联 process 当成成功数据。

输入是同一最终 ac1 完整候选、已完成的全 mean/target 闭盒报告、两个明确
物理 nonmean trial PPoly，以及实际腰振幅行乘子。输出是精确 mean 回填后
整个 \([0,25/8]\) 的连续体 residual 界、两个 mean 的完整迹和所有
nonmean trial jumps。完整真物理边界 residual、boundary adjoint、
\(b_4\) 和全 Schur 仍显式留给后续边界消费，不能从 body-only complete 推出。

## 1. 同一个物理未知，全部数据身份

源：
[scripts/fourfold_codazzi_mean_completed_head_body_residual.py](../scripts/fourfold_codazzi_mean_completed_head_body_residual.py)。

背景仍是 candidate SHA256
\(\mathtt{ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413}\)。
完整候选必须按原 shard loader 校验；没有数组时消费者无法伪造其内容。
mean/target 输入必须是
\(\texttt{actual_final_complete_scalar_mean_Green_cached_full_target}\) 的
**完整**报告，其原 producer SHA256 准确为
\[
 \texttt{6edd8abf820c4e11a25b496c08d0585fb7c943397e7f919ed3774a0b841b0d93}.
\]
同一候选、整个 \(|\eta|\le10^{-9}\)、全 primitive 尾及完整共同闭覆盖
逐项保留。新细分只复用旧 target 值盒；不声称旧值盒随细分变窄。

两个 trial 均采用已有无损 cubic shard 格式。其 metadata 须显式含：

| 字段 | 值或定义 |
|---|---|
| kind | actual_final_mean_eliminated_trial_v1 |
| role | response 或 adjoint_nonmean |
| coordinates | physical moving nonmean variation; h1 sine(4j phi), h2 cosine(4j phi); mean supplied by exact scalar Green |
| background_candidate_sha256 | 上述完整 ac1 SHA |
| background_exact_alpha / background_exact_nu | 原候选准确 dyadic 参数 |
| modes | 该 trial 的全部有限最高指标 \(N\) |

数组按 \(h_1\) 的 sine \(j=1,\ldots,N\) 和 \(h_2\) 的 cosine
\(j=0,\ldots,N\) 排列。供给的第二分量 mean 及其每片全部 cubic 系数
须**准确为零**。这不是将 true mean 设零：true mean 在下一节完整解出。
旧完整 trial 若有 mean，不得默默删去；须用新明确 metadata 另行输出此投影。

两个 trial 可以有不同的真实径向节点。消费者取其节点、完整背景节点、
原 mean/target 分割及 control 两端的精确共同细分；每一闭盒都留在
各自真实 PPoly 片和原 scalar germ 内。所有二进制数按准确 dyadic 解释。

输入 variation 是物理 \((\delta u,\delta v)\)。
若上游用 normalized 变量，应先将其 nonmean 乘实际 \(\alpha\)；
整个参数 source 在此仍取真实固定物理 \(Q\) 的 \(F_\nu\)。
不得把 normalized 的 mean reference 导数额外塞入这个物理 trial。
其与 normalized 完整列的关系由原 M.14 准确给出。

## 2. 两条真正标量方程

令供给的 nonmean response 为 \(w=(\xi,\zeta_\perp)\)，
供给的 nonmean body adjoint 为 \(\lambda\)。
用原 M.3、M.8 的完整定义，置
\[
 B=2\beta m\langle u\xi+K(v-m)\zeta_\perp\rangle,\quad
 g=\langle a_{\rm int},\lambda\rangle,\quad
 c_m=\beta(1-\langle u^2\rangle-K\langle(v-m)^2\rangle-3Km^2).
\]
真实物理 mean 参数源为
\[
 F_{\nu,0}=-\beta mK_{\nu,\rm par}
              (m^2+\langle(v-m)^2\rangle),\quad
 K_{\nu,\rm par}=-Kw+\frac{\beta w'}{2\gamma^2a^2}.
 \tag{D.1}
\]
这里右侧紧支 bump 用 \(w(r)\)，与 response 向量不同义。

响应 mean 准确定义为
\[
 z'=c_mz+F_{\nu,0}-B,\qquad
 z(R)=\ell_R\zeta_\perp(R).                              \tag{D.2}
\]
它是已证真实 nonlinear regular mean 图的 homogeneous derivative。
独立 \(f_B\) 背景仍在原允许类中；本参数 response 取方向
\(\delta f_B=0\)，而不是将背景 \(f_B\) 设零。
因为参数控制在外端恒为零，这条参数 response 没有显式外 mean 源。

消费者用已付
\[
 |\ell_R\zeta_\perp(R)|
 <1.084\,10^{-6}\|\zeta_\perp(R)\|_{L^2_\phi}
\]
包住这个**真实**边界值。它不是将其替换为0，也不需要未取得的
whole-body inverse。对确定的真实外图，(D.2) 有唯一精确标量解；
区间回传包含该解，可能比实际值宽。

若腰振幅乘子是明确给定的准确有理数 \(\lambda_{\rm amp}\)，则 mean adjoint
准确定义为
\[
 \mu'=-c_m\mu-g,\qquad
 \mu(0)=\lambda_{\rm amp}D\mathcal A(v_0)[1].             \tag{D.3}
\]
初值使用
[实际腰 mean 列](R133-supplement-final-waist-mean-column-for-adjoint-lift.md)
完整8门报告；整个未知 Wiener 球、whole-\(\eta\) 和准确报告身份都保留。
没有用猜测的零初值。

这两条 ordinary ODE 的 mean 都连续跨过原 trial/candidate 的有限接缝；
供给的 nonmean PPoly 仍允许真实 jumps。变系数可在这些接缝跳跃，
但这里不产生额外 Dirac mean 源。
原 \(\tau\) 表示的乘法接口已在其完整恒等式中支付；
不能把它们误加成 ordinary \(z,\mu\) 的跳。

## 3. 整个闭盒上的 scalar flow，而非节点 Euler 步

在闭盒上已知 \(A(r)\in A\)、\(b(r)\in B\)，考虑
\(y'=A(r)y+b(r)\)、长度 \(\ell\)、起点区间 \(Y_0\)。
令
\[
 \varphi_1(x)=\int_0^1e^{tx}\,dt=(e^x-1)/x,\qquad\varphi_1(0)=1.
\]
由真实变系数 variation-of-constants，完整端点和整盒解分别包含于
\[
 e^{\ell A}Y_0+\ell\varphi_1(\ell A)B,\qquad
 e^{[0,\ell]A}Y_0+[0,\ell]\varphi_1([0,\ell]A)B .
 \tag{D.4}
\]
证明只用每个积分指数位于对应 scalar 区间，以及指数权恒正；
没有假设 \(A,b\) 在盒内是常数或相互独立的采样值。

源码用完整 Taylor 级数加几何尾计算 \(\varphi_1\)，也与其正积分界
\([e^{\min(0,x_-)},e^{\max(0,x_+)}]\) 相交。
当级数收敛费用或盒宽门不闭时明确拒绝，保留失败；
不会用除以一个含零的 \(x\) 绕过 \(\varphi_1(0)\)。

(D.3) 正向消费 \(A=-c_m,B=-g\)。
(D.2) 从右向左，使用真实反向时间
\(A=-c_m,B=-(F_{\nu,0}-B)\)。
所有先前 endpoint 区间连贯传到下一盒，不在接缝重新初始化。
这给整条精确 mean 解的闭盒包络。

## 4. 完整 body residual 与准确 mean 消减

在整盒包络中，令
\[
 h=w+ze_2,\qquad \psi=\lambda+\mu e_2,
\]
\[
 h_r=w_r+(c_mz+F_{\nu,0}-B)e_2,\qquad
 \psi_r=\lambda_r+(-c_m\mu-g)e_2.
 \tag{D.5}
\]
\(w_r,\lambda_r\) 是真实保存 cubic 的导数，不用待证 PDE 替代它们。
计算原完整 moving 算子及其原伴随：
\[
 R_h=\mathcal Dh-F_\nu,\qquad R_\psi=\mathcal D^*\psi .
 \tag{D.6}
\]
原 \(I\) 及 rank-one mean 项全部使用已发表的完整公式。
(D.2)–(D.3) 证明两个第二平均**准确为零**。
源码先要求原区间计算确实包含这个0，再用已证恒等式投影该单个
coefficient；其它模式全部保留。它不将未知或数值 residual 任意置零。

当前 background 是32模。输入 response/adjoint 分别为 \(N_h,N_\psi\) 模时，
\(\mathcal Dh\) 和 \(\mathcal D^*\psi\) 支持分别最多
\(N_h+64,N_\psi+64\)，\(F_\nu\) 支持最多96。
计算网格严格包含完整 support，没有将未保留输出截回 trial。
圈平均配对直接用完整系数
\(\sum_jf_jg_{-j}\)，不为这个平均作可能混叠的全乘积截断。

输出每盒的完整 \(A^0,A^\sigma,L^2,H^{1/3},H^1\) residual 界，
以及真实有符号
\[
 \int\langle\lambda,R_h\rangle,\qquad
 \int\langle\psi,F_\nu\rangle .                         \tag{D.7}
\]
每个 Fourier 模和两个频率符号均包括在 Parseval/完整和中；
最后再按整径向闭盒作 \(L^2_r\) 或 \(L^1_r\) 累积。
(D.7) 尚不是 \(S_{\rm corr}\)：其真实端点行和 jump 配对尚需下一段。

所有 nonmean response 和 adjoint 的 PPoly jumps 用准确 dyadic Horner
逐接口求出，保存完整 \(A^\sigma,L^2,H^{1/3},H^1\) 的 \(\ell^1\) 费用。
其 reconstructed mean jump 准确为0。没有把原有限图样当作径向连续对象。

## 5. 可恢复步骤、输入方式和下一真实边界门

消费者按五种完整阶段行推进：

1. 每个实际共同闭盒的 scalar 系数和强迫；
2. 全部正向 mean adjoint 闭盒；
3. 全部反向 mean response 闭盒；
4. 完整 Fourier body residual 闭盒；
5. 两个 trial 的全部准确 nonmean jumps。

每次可用 \(\texttt{--max-new-rows 64}\) 保存一个成功前缀，后续新输出
用 \(\texttt{--resume}\) 继续。只有同源、同全部输入、同物理 coordinates、
同真实 row 域和方向才接受。原失败或已完成输出不被覆盖。

~~~sh
PYTHONPATH=scripts python scripts/fourfold_codazzi_mean_completed_head_body_residual.py \
  --candidate /path/to/exact-ac1-candidate.json \
  --mean /path/to/complete-actual-mean-native.json.gz \
  --response /path/to/physical-nonmean-response.json \
  --adjoint /path/to/nonmean-body-adjoint.json \
  --amp-multiplier NUMERATOR/DENOMINATOR \
  --max-new-rows 64 --out notes/new-head-mean-completed-part001.json.gz
~~~

complete 仅表示上述 **body** 合同全部完成。
输出始终明确标记 true physical boundary residual、boundary adjoint、
原 \(b_4\) 和全 Schur 未由本程序支付。
下一消费者必须使用原完整物理矩、真实 nonlinear regular 差、
mean 预处理 \(\omega_R^{-1}\)、真实腰振幅、全部 endpoint 乘子和 jumps，
才可组成原 M.18 双残差门。
环境尚不可用，当前没有该源码的 native 成功声明，也没有不存在的 trial 文件。
