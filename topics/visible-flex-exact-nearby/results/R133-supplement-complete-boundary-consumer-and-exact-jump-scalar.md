# R133 补篇：完整物理边界消费者与全部准确接口校正

2026-11-14。本文给出可重算的实际消费者，
把已完成的 mean/body 消费合同接到全部原物理边界和有符号接口配对。
源在运行环境失联期间完成；**没有已执行 native、实际 trial 或已认证
完整 BVP 逆的声明**。它不会把 finite mean-filled body 的 complete
标志冒充边界已经完成。

源：
[scripts/fourfold_codazzi_mean_completed_physical_boundary.py](../scripts/fourfold_codazzi_mean_completed_physical_boundary.py)。

数学入口是
[完整物理转置与 Schur 配对](R133-supplement-complete-physical-boundary-transpose-and-Schur-pairing.md)
的 P.1–P.28，以及
[完整 mean 回填 body 消费](R133-supplement-mean-completed-head-and-adjoint-body-consumer.md)
的 D.1–D.7。下文补足消费者所用的全部相位余项、原物理模尾和输入规范。

## 1. 输入身份与实际完整未知

背景仍是最终 ac1 中心，准确 \(\alpha,\nu\)、全 \(|\eta|\le10^{-9}\)
及所有 intrinsic primitive 尾不变。全部 candidate shards 必须经原
loader 校验，6145个真实径向节点和32个有限 moving 模均保留。
消费者拒绝仅有 reconstruction manifest、错误对象、错误 normalized
坐标或没有完成 mean/body 闭覆盖的输入。

必须给出：

1. 原完整 ac1 candidate；
2. 同一 candidate、response、adjoint 的完整 mean-filled body 报告，
   producer SHA256 固定为
   \(\mathtt{190291987e288beaa9647afd90b54f16df2c6610d706fee01cac4623e1a4b62f}\)；
3. body 使用的完整实际 mean/target 报告及两个完整 physical nonmean trial；
4. 同一实际 \(R=25/8\) regular/long 端口 native；
5. 已执行的真实腰坐标、腰 mean 列和10门物理转置有理报告；
6. 新明确的 finite **物理** retained Robin dual。

两个 trial 的原无损 cubic 格式、均值恒零及角色身份严格沿用 D.1；
true response mean \(z\) 和 true adjoint mean \(\mu\) 从完整 scalar 解
报告取值，不由新程序猜测，也不再置零。
所有输入采用 physical \(h=(\delta u,\delta v)\)，不暗中消去
normalized 的 \((0,s_\nu)\) 列。

新的外 dual 文本具有以下明确 schema：
~~~json
{
  "kind": "actual_final_physical_retained_Robin_dual_v1",
  "coordinates": "physical cosine-amplitude dual; original physical m=4 output omitted; no alpha normalization",
  "background_candidate_sha256": "ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413",
  "background_exact_alpha": "6890507429876859/9007199254740992",
  "background_exact_nu": "-2572625729470897/72057594037927936",
  "physical_frequency_factor": 4,
  "omitted_physical_mode": 4,
  "modes": 2,
  "cosine_amplitude_multipliers": ["0", "EXACT_RATIONAL"]
}
~~~
这个展示只是 schema，不是实际 trial；末项须由真正 producer 填入。
允许任意实际 finite 最高指标。列表按物理 \(4j\) 排列，
第一项准确为0，其余每项是 real cosine **幅度行**的乘子。
消费者据此建立
\[
 \lambda_R(\theta)=2\sum_j\lambda_j\cos4j\theta,\qquad
 w_R=2\cos4\theta-\lambda_R.
 \tag{C.1}
\]
前面的2及 normalized 行可能需要的 \(1/\alpha\) 不能丢失。
没有输入的“默认已解伴随”不会被自动生成。

## 2. 不混叠的完整 Laurent 代数

每个角对象表示为实际 finite Laurent 多项式 \(P\)，加完整
Wiener \(A^0\) 误差 \(e\ge0\)：
\[
                  f=P+E,\qquad \|E\|_{A^0}\le e .
\]
所有 finite 系数均用 Arb/Acb 外包。乘积使用普通
\(\operatorname{acb\_poly}\) 卷积，保留全部系数；
没有循环 FFT 截断，也没有角采样代替整圆。
若 \(f=P+E,\ g=Q+F\)，完整乘积余项为
\[
 \|P\|_{A^0}e_F+\|Q\|_{A^0}e_E+e_Ee_F.                \tag{C.2}
\]
加法、标量除法、频率平移、复共轭和完整 mean 均保留其余项。
\[
 \|IE\|_{A^0}\le e/4,\qquad
 \|P_{\ne0}E\|_{A^0}\le e,\qquad
 \|E\|_{L^2}\le e.
 \tag{C.3}
\]
源码禁止对只有 \(A^0\) 误差的对象直接微分，亦禁止将其免费提升到
带角权的范数。实际需要的 \(b_\theta,c_\theta\) 从完整 finite
**物理权**先精确微分，再作相位复合。

对实际 finite \(p\)，若 \(M=\|p\|_{A^0}\)，以
\(E_n=\sum_{\ell=0}^n p^\ell/\ell!\) 近似 \(e^p\)。当
\(M/(n+2)<1\) 时，完整余项为
\[
 \|e^p-E_n\|_{A^0}
 \le \frac{M^{n+1}}{(n+1)!}
                 \frac1{1-M/(n+2)}.                  \tag{C.4}
\]
实际默认要求该数小于 \(2^{-180}\)；未闭合则明确失败。
(P.4) 的所有角复合使用 (C.4)，所以真实物理 Fourier 无限尾仍存在于
显式误差中，绝非截为 finite moving 模。

腰端的完整 nonmean 幅度梯度直接计算
\[
 G_{{\cal A},\perp}
       =\frac8{m_0^2}I\sin(4\phi+4\psi_0).            \tag{C.5}
\]
其 mean 使用已经执行的完整腰 mean 列报告。
因此真实幅度方向为
\[
 D{\cal A}[h_2(0)]
 =\langle G_{{\cal A},\perp},w_2(0)\rangle
                           +b_{{\rm amp},m}z(0).
 \tag{C.6}
\]
消费者明确保留后一项；腰 odd Dirichlet 的 residual 和有符号配对也另行保存。

## 3. 全物理方向矩

实际 outer reference \(s_R\) 取同一完整 regular 端口 native。
所有 endpoint cubic 均按输入 double 的准确 dyadic 值用有理 Horner
评价，非mean trial 亦如此。腰上真实 \(a'(0)=0\)，故准确
\(s_0=-a_0\)；其完整 target 区间消费原23门腰报告，全部实际
\(V_j(0)\) 再与该报告的准确 dyadic 向量逐项相同。于是 \(u,v,m,\psi,h\) 是确定的 finite
moving 多项式及已支付的标量区间。

令 \(k=4j>0\)，\(\Theta_h=I(h_2-zv/m)/m\)。完整原物理矩的变分为
\[
 \delta C_k=-\frac z m C_k
       -\frac{ik}{m}\langle e^{-ik(\phi+\psi)}\Theta_h\rangle,
\]
\[
 \delta B_k=-\frac z m B_k
       +\frac1m\langle e^{-ik(\phi+\psi)}
                                (h_1-iku\Theta_h)\rangle.
 \tag{C.7}
\]
这里
\(C_k=m^{-1}\langle e^{-ik(\phi+\psi)}\rangle\)、
\(B_k=m^{-1}\langle ue^{-ik(\phi+\psi)}\rangle\)。
背景 \(C_k\) 的计算先用 \(e^{-ik\psi}-1\)，保留准确非mean 消去。
同时保存完整背景的 \(C_k,B_k\)，以同一全物理模式尾重新检查
\(\|Z\|_{A^0}<10^{-12}\) 的真正 nonlinear derivative 入球门。
没有读取失联的旧 endpoint binary 或假定该入球自动成立。

每个矩直接读取 (C.4) 完整多项式的第 \(j\) 个 Fourier 系数，
再加全部 Wiener 余项；没有假设任何梯形积分准确。
真实反射给 \(\delta C_k\) 实、\(\delta B_k\) 纯虚。
源码先要求区间包含相应准确零，再按已知反射恒等式使用它们。

因此实际 proposal Robin 正模是
\[
          R_{{\rm num},k}=i\,\delta B_k+q_{\rm num}\delta C_k.
 \tag{C.8}
\]
计算 retained 范数时只去掉原物理 \(k=4\)，其余完整正负模式保留。
它不在 moving Fourier 的第四槽操作。
暂列输出的 true \(b_4\) 仍单独报告，并保留完整 DN/regular 误差。

## 4. 所有未计算物理模式的完整费用

设实际保留物理正指标至 \(J\)，取 \(0<\sigma\le1/8\)，并记
\[
 P=\|\psi\|_{A^\sigma},\quad
 U=\|u\|_{A^\sigma},\quad
 H=\|h_1\|_{A^\sigma},\quad
 T=\|\Theta_h\|_{A^\sigma},\quad
 d=\sigma-P>0,\quad a_m=1/|m|.
\]
这些量全部由实际 finite moving 系数与真实 target/mean 区间计算；
输入有限不意味着物理输出有限。

按每个系数的复圆周移位，(C.7) 给
\[
 |\delta C_k|\le kC_1 e^{-kd},\qquad
 |\delta B_k|\le(B_0+kB_1)e^{-kd},                     \tag{C.9}
\]
其中
\[
 C_1=|z|a_m^2P+a_mT,\quad
 B_0=|z|a_m^2U+a_mH,\quad B_1=a_mUT.
\]
故 \(|R_{{\rm num},k}|\le(R_0+kR_1)e^{-kd}\)，
\(R_0=B_0,\ R_1=B_1+q_{\rm num}C_1\)。
这是每一个未保留 \(k\) 的真界。
同一式给背景双号尾
\(8a_mPG_1\) 和 \(2a_mUG_0\)，与已算背景物理矩共同支付上述入球门。

令 \(x=e^{-4d}\)、\(n=J+1\)：
\[
 G_0=\frac{x^n}{1-x},\quad
 G_1=x^n\left(\frac n{1-x}+\frac x{(1-x)^2}\right),
\]
\[
 G_2=x^n\left(\frac{n^2}{1-x}+
       \frac{2nx}{(1-x)^2}+\frac{x(1+x)}{(1-x)^3}\right).
\]
完整双号尾分别满足
\[
 \|\delta Z_{>J}\|_{A^0}\le8C_1G_1,\qquad
 \|R_{{\rm num},>J}\|_{A^0}
                    \le2(R_0G_0+4R_1G_1),             \tag{C.10}
\]
以及同时控制 \(0\le s\le1\) 的
\[
 \|\delta Z_{>J}\|_{H^s}\le8C_1(G_1+4G_2),
\]
\[
 \|R_{{\rm num},>J}\|_{H^s}
 \le2\{R_0G_0+4(R_0+R_1)G_1+16R_1G_2\}.             \tag{C.11}
\]
这里用 \((1+k^2)^{s/2}\le1+k\) 和完整加权 \(\ell^1\) 控制
\(\ell^2\)。低模式则按实际 Parseval 权 \((1+k^2)^s\) 累加。
源码分别报告 \(L^2,H^{1/6},H^1\)，都含全部未知物理尾。

[实际 \(H^s\) long 图](R133-supplement-final-regular-Hs-and-Riccati-outer-graph.md)
给
\[
 \|\delta Z\|_{H^s_\theta}<.03\|h_2\|_{H^s_\phi},
 \quad
 L_{d,0}<5.898255\,10^{-6},\
 L_{d,1/6}<1.11\,10^{-5},\
 L_{d,1}<1/4000 .
\]
因此每个 retained physical primal residual 的完整费用是
\[
 (L_{d,s}+\epsilon_{\rm prop})\|\delta Z\|_{H^s},
 \qquad \epsilon_{\rm prop}=9.1496\,10^{-18}+2^{-512}.  \tag{C.12}
\]
(C.12) 与 (C.10)–(C.11) 的独立 \(\delta Z\) 上界可取较小者。
未知 true nonlinear DN 的频谱从未被截断。

## 5. 完整物理转置、全部准确 jumps 和同一个标量

外 dual 使用实际 \(w_R\)，按 (P.4) 计算其完整相位梯度。
mean 对偶行由准确
\[
 \lambda_{\rm mean}
       =(\langle w_R,{\cal R}e_2\rangle-\mu(R))/\omega_R
\]
回填；消费者以已执行预算包住它，保留原 \(\omega_R^{-1}\)。
完整 nonmean 转置误差付
\(1.77\,10^{-7}\|w_R\|_2+1.106\,10^{-6}|\mu(R)|\)，不把它设零。

所有 response 接口准确计算
\[
 J_{\rm resp}=\sum_i
 \langle\lambda(r_i^+),w(r_i^+)-w(r_i^-)\rangle ,
 \tag{C.13}
\]
另记录全部 adjoint 接口的
\[
 J_{\rm dual}=\sum_i
 \langle\lambda(r_i^+)-\lambda(r_i^-),w(r_i^-)\rangle.
 \tag{C.14}
\]
两个真实节点网格可不同。每次使用实际左/右 PPoly 片，
每个 double 按准确有理数处理；nonmean sine/cosine Parseval 各带
\(1/2\)。重构后的 ordinary mean 连续，所以其 interface 项准确为零。
没有把候选 \(\tau\) 表示的乘法 jumps 误加到 ordinary mean 中。

模型 corrected scalar 完整组装为
\[
\begin{split}
 S_{\rm mod}={}&\sum_{j>0}(w_R)_j^{\cos}
                                    R_{{\rm num},4j}\\
 &-\langle\lambda_1(0),w_1(0)\rangle
 -\lambda_{\rm amp}D{\cal A}[h_2(0)]
 -\int\langle\lambda,R_h\rangle\,dr-J_{\rm resp}.
\end{split}                                                   \tag{C.15}
\]
有限 \(w_R\) 的每一项都在已算物理矩范围内。
全部 mean 和完整 body 积分使用原证书包络。
真正 \(S_{\rm corr}\) 在
\[
 S_{\rm mod}\ \mathbin{\pm}\
 1.77\,10^{-7}\|w_R\|_2\|P_\perp h_2(R)\|_2             \tag{C.16}
\]
内。输出将明确区分“校正标量区间排除零”和“真正 \(\nu\) Schur
非零”；前者仍不足以推出后者，完整 inverse/双残差乘积门仍不可省。

## 6. 恢复和范围

~~~sh
PYTHONPATH=scripts python scripts/fourfold_codazzi_mean_completed_physical_boundary.py \
  --candidate /path/to/exact-ac1-candidate.json \
  --body /path/to/complete-mean-filled-body.json.gz \
  --mean /path/to/complete-actual-mean-native.json.gz \
  --response /path/to/physical-nonmean-response.json \
  --adjoint /path/to/nonmean-body-adjoint.json \
  --outer-dual /path/to/explicit-physical-retained-dual.json \
  --moments 256 --max-new-rows 64 \
  --out notes/new-complete-physical-boundary-part001.json.gz
~~~

完整端点行、每个 physical moment、每个 exact jump 都作为独立完成行保存。
通过 \(\texttt{--resume}\) 只恢复同源、同全部输入和同实际范围的成功前缀；
原失败或完整报告不覆盖，不猜丢失执行的退出状态。
默认64行一片，避免一次长进程丢失全部已成数据。

最终 complete 仅授予这里列出的边界、物理模尾、有符号跳和
corrected scalar 数量。原 full body certificate 仍保持自己的身份；
程序不会重写它或将其不完整旗标改为完整。
实际 response/adjoint 目前尚未取得，故本文没有 native 成功值，
没有无穷频 whole BVP inverse，也没有真正参数 Schur 非零的结论。
