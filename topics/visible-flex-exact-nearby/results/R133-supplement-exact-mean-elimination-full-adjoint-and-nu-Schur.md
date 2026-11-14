# R133 补篇：精确消去完整平均模后的补逆、伴随及真正参数 Schur

2026-11-14。本文构造完整平均模的精确消元及其伴随回填，保持已经选定的
**物理外端四次 Robin 行 \(b_4\) 暂列输出**，不另换一个未经比较的标量问题。
完整外 mean 的 canonical 端口预算实际执行 18 个 BigInt 有理门，全部通过。
整个径向 \(\Gamma\)、非平均补逆及真正 \(\nu\) Schur 数值仍未完成，范围见 §7。

对象始终是最终 full-\(R\) moving 候选
\(\mathtt{ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413}\)，
\(R=25/8\)，完整原 \(|\eta|\le10^{-9}\)，固定准确 \(\alpha,\nu\)。
这里只在线性未知中分开平均分量，没有将有限 moving Fourier 误当成物理 Fourier。

## 1. 固定原补空间，明确两类未知和全部行

使用
[完整 moving 算子](R133-supplement-complete-moving-band-and-mean-parameter-Schur.md)
B.1–B.13。记
\[
 Q=(u,v),\quad m=\langle v\rangle,\quad
 J=\begin{pmatrix}0&K\\-1&0\end{pmatrix},\quad
 \mathcal D=\partial_r-\mathcal A .
\]
在真实反射类中写
\[
 h=(\xi,\zeta)=w+z e_2,\qquad
 w=(\xi,\zeta_\perp),\quad\langle\zeta_\perp\rangle=0,\quad
 z=\langle\zeta\rangle .
 \tag{M.1}
\]
\(\xi\) 奇、\(\zeta_\perp\) 偶；仅奇 mean 由反射为零，偶 mean 仍是未知。

令 \(\overline A\) 包含全部体方程、全部接口、腰奇条件、真实物理振幅行、
全部真实外 mean 和除 \(b_4\) 外的所有非mean 外行，恰如
[腰坐标篇 A.17](R133-supplement-final-waist-amplitude-coordinate-and-mean-Schur.md)。
\(b=D_Qb_4\) 仍是原物理行，含 true regular、nonlinear cap 和完整角矩。
下文不会直接把 moving Fourier 的第四行换作这个输出。

将 mean 的体行、外 mean 行和 mean jumps 一起列为第二组数据；
其余全部保留行为第一组。先对外 mean 行作 §2 明确的可逆标量
预处理 \(\mathcal P\)，其它行不变，准确有算子块表示
\[
 \mathcal P\overline A=
 \begin{pmatrix}\mathbb A&\mathbb C\\
                 \mathbb B&\mathbb T\end{pmatrix},
 \qquad b=(b_w,b_z).
 \tag{M.2}
\]
\(\mathbb C\) 包含体区 mean 列，也包含腰振幅和原物理外行的真实 mean 列。
因此它不是仅一个有限 Fourier 乘子。
\(\mathbb B\) 同样包括实际外 mean 功能的完整高频部分。

## 2. 真正标量逆和体内有限支持

令
\[
 c_m=\beta(1-\langle u^2+Kv^2\rangle-2Km^2),\qquad
 B_{\rm int}w=2\beta m
      \langle u\xi+K(v-m)\zeta_\perp\rangle .
 \tag{M.3}
\]
完整 mean 体行为
\[
 (\partial_r-c_m)z+B_{\rm int}w=f_0+F_{\nu,0}\delta\nu,\qquad
 F_{\nu,0}=-\beta mK_{\nu,\rm par}\langle v^2\rangle .
 \tag{M.4}
\]
它没有把平均目标参数源或非平均反馈删除。

[真实 \(H^s\) 外图](R133-supplement-final-regular-Hs-and-Riccati-outer-graph.md)
S.28–S.29 给准确 mean 图
\[
 z(R)=\ell_R y_R+g_R,\qquad y_R=\zeta_\perp(R).
 \tag{M.5}
\]
\(\ell_R=-m_R^2D_Zc_0\Psi^{-1}\) 是完整无限维功能。
\(\Psi\) 只从 \(\delta C\) 及真实 mean 图构造；它不需要先将第四
非mean Robin 行设零。因此 (M.5) 可合法用于当前仍把 \(b_4\) 暂列
输出的补空间。

明确原物理 mean 行的预处理：在固定中心，完整物理非mean变化可写
\(\delta Z=\mathcal Z_y y_R+\mathcal Z_z z_R\)，其中两列由真实角矩/逆变分
给出。原 mean 残差是
\[
 \omega_R z_R-D_Zc_0\mathcal Z_y y_R,\qquad
 \omega_R=-m_R^{-2}-D_Zc_0\mathcal Z_z.
 \tag{M.5a}
\]
原已付逆变分给 \(\|\mathcal Z_z\|_{L^2}<.03\)。因此
\[
 |m_R^2D_Zc_0\mathcal Z_z|
 <49(.03)(7.372818\,10^{-7})<1.1\,10^{-6},\quad
 \omega_R<0,\quad |\omega_R^{-1}|<50 .
 \tag{M.5b}
\]
令 \(\mathcal P\) 仅将这一个原 mean 行乘 \(\omega_R^{-1}\)。
准确有
\[
 \ell_R=\omega_R^{-1}D_Zc_0\mathcal Z_y,\qquad
 g_R=\omega_R^{-1}(D_{f_B}c_0\,\delta f_B+r_C).
 \tag{M.5c}
\]
它与 \(\Psi\) 表示等价，完整 \(f_B,r_C\) 仍存在。
所有数据列随同预处理，物理输出 \(b_4\) 保持原样。伴随回填时
原物理 mean 边界乘子是预处理后的乘子再乘 \(\omega_R^{-1}\)；
不能把这个标量变换漏掉。

准确指定
\[
 \mathbb T z=((\partial_r-c_m)z,\ z(R),\ [z]_i),\qquad
 \mathbb B w=(B_{\rm int}w,\ -\ell_Ry_R,\ 0).
 \tag{M.6}
\]
对有界分片 \(c_m\)，\(\mathbb T\) 的解算子 \(\mathbb G\) 是唯一的
ordinary 一阶标量 Green。若数据为 \((f,g,j)\)，则
\[
 (\mathbb G(f,g,j))(r)
   =H(r,R)g-\int_r^R H(r,t)f(t)\,dt
                       -\sum_{r<r_i<R}H(r,r_i)j_i ,
 \quad H(r,t)=e^{-\int_r^t c_m}.
 \tag{M.7}
\]
所有 mean response jumps 都是独立数据；它们不等于候选 \(m\) 的跳。

为实际有用的数值界，必须使用
[平均模三角 Green 篇](R133-supplement-complete-mean-triangular-Green-and-cached-consumer.md)
的真实 \(\tau=-2a^2/m^3\)、残差 \(\widetilde c\) 和全部候选乘法 jumps。
其 \(H\) 与 (M.7) 准确相同；这一步不是把候选视为真解。
该篇给完整 \(L^2\) 源、体区输出、腰迹和 response jumps 的界。
\(\Gamma\) 尚未运行完之前，不能将它置为1。

体区 mean 列准确为
\[
 a_{\rm int}
 =P_\perp\{Le_2-2\beta KQ_\phi I(v-m)+\gamma JQ_\phi\},
 \quad
 P_\perp\mathcal D(w+ze_2)
       =P_\perp\mathcal Dw-a_{\rm int}z .
 \tag{M.8}
\]
这个式子不使用中心残差为零。\(P_\perp\) 只从第二分量去 mean。

已发表的 B.6、B.9–B.13 立即给：
\(B_{\rm int}\) 只读 \(|j|\le32\)，\(a_{\rm int}\) 输出 \(|j|\le64\)，
完整 \(F_\nu\) 支持 \(|j|\le96\)；
normalized 附加背景列 \(\mathcal D(0,s_\nu)\) 支持 \(\le64\)。
这些是已付的准确支持事实，不是本文新增数值验证。

所以消去 mean 后，**纯体内** \(\mathbb C_{\rm int}\mathbb G
\mathbb B_{\rm int}\) 是角头部反馈。由 \(\ell_Ry_R\) 产生的高频外输入
仍完整进入这个反馈；不能因为 (M.8) 的输出有限就删除其无限维输入。
原物理腰振幅和外非mean 行也仍是完整泛函。
原 193 个 angular head 未知只在此意义下少去一个径向 mean 函数：
得到 192 个非mean head 分量及显式径向积分，加入 \(\nu\) 为193。
它仍是径向、含积分的 BVP，不是一个已经认证的193阶常数矩阵。

## 3. 精确 Schur 消去和真正 \(\nu\) 列

把实际未规范化体源写成 \(F_\nu=\partial_\nu\mathcal F\)，令
\[
 f=(f_w,f_m),\qquad F_\nu=(F_w,F_m)
\]
表示经过同一 \(\mathcal P\) 的两组完整数据；\(F_m\) 包含 (M.4)，其外边界和接口显式列为零，
因为控制支集严格在体区内部。

定义
\[
 \mathbb S=\mathbb A-\mathbb C\mathbb G\mathbb B,\quad
 \widehat f=f_w-\mathbb C\mathbb Gf_m,\quad
 \widehat F=F_w-\mathbb C\mathbb GF_m,
\]
\[
 \widehat b=b_w-b_z\mathbb G\mathbb B .
 \tag{M.9}
\]
参数数据和普通数据都作同一预处理后，完整解等价于
\[
 \mathbb S w=\widehat f+\widehat F\,\delta\nu,\qquad
 z=\mathbb G(f_m+F_m\delta\nu-\mathbb Bw).
 \tag{M.10}
\]
原暂列输出是
\[
 b[h]=\widehat b[w]+b_z\mathbb Gf_m
                           +b_z\mathbb GF_m\,\delta\nu .
 \tag{M.11}
\]
普通 mean 源、独立外 mean、response jumps 和所有 \(f_B\) 数据
通过这些式子保留。不存在一个可以先删除的“零模”。

若 \(\mathbb S^{-1}\) 已在实际同一全空间支付，令
\(w_\nu=\mathbb S^{-1}\widehat F\)，则
\[
 \boxed{\mathscr S_\nu=
       \widehat b[w_\nu]+b_z\mathbb GF_m.}               \tag{M.12}
\]
这与原 \(\overline A\) 的标量完全相同。
这里原输出 \(b_4\) 只作用外端，而 \((\mathbb GF_m)(R)=0\)，所以
当前紧支控制有准确的 \(b_z\mathbb GF_m=0\)。
这是**外端输出位置和参数支集**造成的准确零，不是参数 mean 被删去。

尤其，腰物理振幅行是 \(\mathbb A,\mathbb C\) 的保留行。
若其 mean 系数为 \(b_{{\rm amp},m}\)，则 \(\widehat F\) 在该行准确包含
\[
             -b_{{\rm amp},m}(\mathbb GF_m)(0).
 \tag{M.13}
\]
这项一般不为零。参数 mean 的全部径向回传仍影响真正低标量；
不能因 (M.12) 的末项在外端为零就遗漏 (M.13)。

若改在 normalized \((U,V)\) 中运行，仍须用此前已证完整列
\[
 \alpha^{-1}\{\mathcal D(0,s_\nu)-F_\nu\}.
 \tag{M.14}
\]
先明确把物理变化 \(h=\alpha h_{\rm norm}+(0,s_\nu)\delta\nu\) 代入，
再作 (M.9)；不能只将 \(F_m\) 除以 \(\alpha\) 而漏掉 \(s_\nu'\)。
控制在腰和外端恒零，故两个端点的显式 reference 列也准确为零。

## 4. 精确回填伴随 mean，双残差门保持不变

所有转置/对偶都在同一实际状态、源和 trace 空间中取；
标量 Green 没有角导损。令 \(\lambda\) 是非mean 第一组数据的任意 trial
伴随，定义
\[
 \mu=\mathbb G^*(b_z^*-\mathbb C^*\lambda).
 \tag{M.15}
\]
则预处理后 trial \((\lambda,\mu)\) 的 mean 对偶行**准确满足**
\[
 \mathbb C^*\lambda+\mathbb T^*\mu=b_z^*,
\]
而唯一剩余的对偶误差是
\[
 b_w^*-\mathbb A^*\lambda-\mathbb B^*\mu
       =\widehat b^*-\mathbb S^*\lambda .               \tag{M.16}
\]
证明直接用 \(\mathbb T^*\mathbb G^*=I\)。
原物理数据上的完整 trial 为
\(\Lambda=(\lambda,\mu)\mathcal P\)。因此不必再用不完整的有限转置来近似一个独立 mean adjoint。
这里 \(\mu\) 包含 mean 体源、真实外 mean 和每一个 response jump 的乘子。

为给可计算公式，设实际功能
\[
 (b_z-\lambda\mathbb C)[z]
       =c_0z(0)+c_Rz(R)+\int_0^R g(r)z(r)\,dr .
\]
其中 \(g=a_{\rm int}\cdot\lambda_{\rm body}\)；
\(c_0,c_R\) 包含所有保留腰/外行及原物理 \(b_4\) 的 mean 系数。
Fubini 与 (M.7) 得
\[
\begin{aligned}
 \mu_{\rm body}(t)
   &=-c_0H(0,t)-\int_0^t g(r)H(r,t)\,dr,\\
 \mu_R&=c_R+c_0H(0,R)+\int_0^R g(r)H(r,R)\,dr,\\
 \mu_{j_i}&=-c_0H(0,r_i)-\int_0^{r_i}g(r)H(r,r_i)\,dr.
\end{aligned}                                                   \tag{M.17}
\]
所以 \(\mu_{j_i}=\mu_{\rm body}(r_i)\)，
\(\mu_R=c_R-\mu_{\rm body}(R)\)。
该 mean 伴随连续跨过原有限 PPoly 接口；
\(-\mu'_{\rm body}-c_m\mu_{\rm body}=g\)，
\(\mu_{\rm body}(0)=-c_0\)。
原 \(\tau\) 的乘法 jumps 只用于正确计算 \(H\)，没有额外伪造
ordinary mean adjoint 的跳。若实际数据或功能在内部另有原子列，
同一个 (M.7) 转置直接增加其真实项，不能丢弃。

实际浮点/区间实现若只得到 \(\widetilde\mu\)，必须保留
\(\mathbb T^*\widetilde\mu-(b_z^*-\mathbb C^*\lambda)\) 的误差；
(M.15) 的准确零不能授给未经认证的离散积分。

对任意完整 response trial \(\widetilde h_\nu\)，原
[双残差恒等式](R133-supplement-complete-nu-adjoint-and-dual-residual-Schur.md)
仍是
\[
 r_\nu=\overline A\widetilde h_\nu+g_\nu,\quad
 S_{\rm corr}=b[\widetilde h_\nu]-\Lambda r_\nu,
\quad
 \mathscr S_\nu=S_{\rm corr}
      -(b-\Lambda\overline A)[\overline A^{-1}r_\nu].
 \tag{M.18}
\]
(M.15) 只将其中 mean 对偶残差严格消去；非mean 全频残差、
真实 physical boundary、参数 reference 以及全部接口仍完整存在。
它不替代尚未支付的全补逆或数值非零门。

## 5. 外 mean 直接接同一完整 Riccati 高端口

这里消费实际最终
[外 \(H^{1/6}\) 图 S.35–S.38](R133-supplement-final-regular-Hs-and-Riccati-outer-graph.md)，
不再把 \(\ell_R\) 假定有限带。
记 \(Z_{s,H},Z_{u,H}\) 为完整 \(|j|\ge97\) 的同一 Riccati stable/unstable
状态，\(y_L=P_{1\le|j|\le96}y_R\)。
原已付
\[
 \|Z_{u,H}\|
 <2.22\,10^{-5}\|Z_{s,H}\|+2.35\,10^{-5}\|y_L\|
   +3\,10^{-5}F_B+22\|r_B\|_{H^{1/6}}+26|r_C|,
 \tag{M.19}
\]
\[
 |z(R)|<1.084\,10^{-6}\|y_R\|_{H^{1/6}}
                  +4.1\,10^{-6}F_B+50|r_C| .
 \tag{M.20}
\]
这里 \(F_B=\|\delta f_B\|_{\dot H^{2,1/6}}\)，
\(r_B,r_C\) 是真实物理两行 residual。

\(W_M\ge p_*>1/8\) 和准确高端口式给
\[
 \|y_H\|_{H^{1/6}}
 <\frac{51}{16}(\|Z_{s,H}\|+\|Z_{u,H}\|),\qquad
 \|y_L\|_{H^{1/6}}<3\|y_L\|_2 .
 \tag{M.21}
\]
第一式支付 homogeneous/Bessel 比 \(17/16\) 和
\(W_M^{-1/2}<3\)；没有未知正区内部 Riccati 上界。

代入 (M.19)–(M.20) 的五列准确有理数得到
\[
\boxed{\begin{aligned}
 |z(R)|<&\ 3.456\,10^{-6}\|Z_{s,H}\|
       +3.253\,10^{-6}\|y_L\|_2\\
 &+4.101\,10^{-6}F_B
       +7.602\,10^{-5}\|r_B\|_{H^{1/6}}+50.001|r_C|.
\end{aligned}}                                                   \tag{M.22}
\]
这是整个外 mean 的有限秩图，并非只给非mean主部。
如果暂列输出的物理 \(b_4\) 尚未闭合，其对应 \(r_B\) 分量必须继续放在
(M.19)、(M.22) 中；不能在计算真正 \(\nu\) Schur 前先将其设为零。

## 6. 外 mean 向腰振幅的完整、仍含 \(\Gamma\) 的反馈

已付实际端点比给
\[
 H(0,R)<2.693551\,10^{-13}\Gamma.
 \tag{M.23}
\]
仅对外 homogeneous mean 列，(M.22) 与 (M.23) 给下表。
预算实际先乘未向上粗化的五个精确有理数，再比较表中的严格有理上界。

| 输入及原完整范数 | 外 mean 列上界 | 腰 mean 系数，仍须乘 \(\Gamma\) | 腰振幅 mean 系数，仍须乘 \(\Gamma\) |
|---|---:|---:|---:|
| 同一 stable high \(Z_{s,H}\) | \(3.456\,10^{-6}\) | \(9.308\,10^{-19}\) | \(3.2578\,10^{-18}\) |
| 全部非mean head \(y_L\)，\(L^2\) | \(3.253\,10^{-6}\) | \(8.760\,10^{-19}\) | \(3.0659\,10^{-18}\) |
| 独立 \(f_B\)，\(\dot H^{2,1/6}\) | \(4.101\,10^{-6}\) | \(1.1044\,10^{-18}\) | \(3.8654\,10^{-18}\) |
| 真实 physical Robin residual，\(H^{1/6}\) | \(7.602\,10^{-5}\) | \(2.0476\,10^{-17}\) | \(7.1664\,10^{-17}\) |
| 独立 physical mean residual | \(50.001\) | \(1.34678\,10^{-11}\) | \(4.71373\,10^{-11}\) |

最后一列用实际腰整个 \(10^{-6}\) Wiener 球上
\(\|D\mathcal A\|<7/2\)，因此保住纯 mean 方向的真实作用；
它没有把腰振幅等同于原 moving 第一 Fourier 系数。
未知 \(\Gamma\) 必须留在这些系数中。
(M.4) 的体内非mean、参数、普通源和响应 jumps 也都要另按
(M.7) 加入，表格不是完整 \(z(0)\) 或完整 Schur 误差的上界。

## 7. 实际执行、可用范围和剩余工作

源：
[scripts/fourfold_codazzi_mean_eliminated_Schur_ports.mjs](../scripts/fourfold_codazzi_mean_eliminated_Schur_ports.mjs)；

报告：
[18 门完整有理预算](../notes/2026-11-14-R133-mean-eliminated-Schur-ports-rational.json)。

同一完整 BigInt 函数已在当前可用 V8 实际执行；18 个严格门全部通过。
它只消费 §5–6 已发布的同中心文本界，不读取不存在的 binary native，
也不声称恢复了完整 candidate shards。Node 包装可在运行时恢复后重放。

本文给出 \(\mathbb T^{-1}\)、完整 Schur 等价和可准确回填的 mean adjoint，
并把实际外端全频 mean/source 与同一 canonical 高端口接好。
实际 \(\mathbb S^{-1}\)、全径向 \(\Gamma\)、response/adjoint 的连续残差、
真正 \(\mathscr S_\nu\) 非零、far nonlinear label 匹配以及整个闭面目标
仍须分别完成。这些剩余量不能由表中的小端点系数代替。
