# R835：原 p41 的四阶导数层实际终止，原 D 约化

日期：2026-11-15。状态：**公开 Actions 实际完成；原特征零 \(\mathscr I_4=\mathscr C_L\)，原有效除子 \(D\) 约化，安全重数界 \(K=1\)。** 这是原 p41 函数 \(y_{f_4}\) 的结果，不是全部素数的 Serre 一致性证明。原 \(D\) 的准确坐标、\(\eta\)、规范高度及统一排除仍待。

## 1. 实际运行与来源

本结果消费冻结的 [R827 原全球充分证明](R827-original-global-modular-surjectivity-and-derivative-termination.md) 和 [行列式 Bézout 证明](../notes/R827-original-determinantal-Bezout-termination-certificate.md)，不改变它们写作时的历史状态。

| 项目 | 实际记录 |
|---|---|
| 公开运行 | [43767561191](https://github.com/Rogerhu12/math-research-public/actions/runs/43767561191) |
| 数学 job | 132976021283 |
| source commit | 3198158aea6a78e32c7e4c62f45ce4b754ac2718 |
| core 时间 | 46.529879230999995 秒 |
| core 结束 | 2026-11-15T22:10:11.282863+00:00 |
| 退出与状态 | exit 0，error null，core 与完整 verify 成功 |
| 真剩余域 | \(\mathbf F_{1000000753}\)，原 branch 0 / free 1186 |
| 实际使用投影 | \(a=0,1\)，到 gcd 1 即停止 |
| 最终成功标志 | original_I4_equals_C=true，safe_D_multiplicity_bound=1 |

原 source 是 R827 run 43734420663、commit 400edecfeab313d1858cdb72bf18f8452ab9566a 已完成的五层 1360 条 \(C\) 坐标列，以及同源无穷远证书。没有重算原导数、原 \(C\) 整除、单位节点、模算子或无穷远秩；旧未完成的多项式 Hermite 不作为这里的证据。

原特征零函数仍为 \(y=y_{f_4}\)，\(L=\mathbf Q(b,\zeta)\)，\(\tau=e_0,\sigma=e_1+e_{73}\)，正规权 \(\epsilon=(0,1^{144},2^{127})\)。原 \(B\) 是单位 Schur chart 的真实整 lift，不把任意模 kernel 向量冒称为特征零函数。原 \(82^{10}\)、\(\lambda\)、\(b/s\)、原导子尺度 6724、两图负号与修正项保持不变。

## 2. 整个第一图的准确证书

按原层和列顺序，令

$$
G(z)=\overline C_\tau^{-1}
 [\,\overline F_{0,\tau},\ldots,\overline F_{4,\tau}\,]
 \in M_{272\times1360}(k[z]),
\qquad
V(a)=\begin{pmatrix}I\\aI\\a^2I\\a^3I\\a^4I\end{pmatrix}.
$$

本运行准确得到 \(d_a(z)=\det(G(z)V(a))\) 的全部系数：

| 投影 | 证明的次数上界 | 全部互异节点数 | 实际次数 |
|---|---:|---:|---:|
| \(a=0\) | 1340 | 1341 | 1320 |
| \(a=1\) | 3516 | 3517 | 3496 |

这些节点为从 0 开始的连续整数，均小于剩余域特征。每个节点都以准确有限域 determinant 计算，零 determinant 也保留。原 weighted 界、\(\sum\epsilon_i=398\) 和 \(\det C_\tau=P_\tau\) 的完整 20 次因子给上述严格界；完整 Newton 插值和所有节点代回认证的是整个 determinant 多项式。

实际扩展 gcd 的第二个前缀给首一 gcd \([1]\)，并完整核实两条保存的多项式系数 \(u_0,u_1\) 满足

$$
u_0(z)d_0(z)+u_1(z)d_1(z)=1.
\tag{835.1}
$$

因此明确的分解式

$$
X(z)=u_0V(0)\operatorname{adj}(GV(0))
     +u_1V(1)\operatorname{adj}(GV(1))
\tag{835.2}
$$

是 \(k[z]\) 上的真实多项式矩阵，且 \(GX=I_{272}\)。这一等式来自已核的完整 determinant、(835.1) 及通用伴随矩阵恒等式。没有展开或声称已经物化 1360×272 右逆的所有系数；机器标志准确为 factored_right_inverse_certified=true、expanded_adjugate_or_right_inverse_materialized=false。

这不是用有限点的满秩猜全局满射：有限点负责在证明的次数界内唯一确定两个完整多项式，随后整个多项式环内的 (835.1) 给右逆。

## 3. 无穷远与原特征零结论

原 R827 已完成的第二图 \(t=0\) 证书给原 272×1360 矩阵秩 272、实际非零子式 695832206；原 \(\det C_\sigma(0)=426224185\ne0\)。新 run 原样消费同源证书，不重计算。

(835.2) 覆盖第一图所有特殊纤维点，原无穷远证书覆盖唯一补点。R827 §3–5 的完整整性、flat cusp target、原齐次 source 与 proper/Nakayama 论证遂给

$$
\boxed{\mathscr I_4=\mathscr C_L,\qquad I_4=\mathcal O_Y(-\mathcal D_{\rm cusp}).}
\tag{835.3}
$$

这里 cusp 除子只有原 20 个尖点，不包含 \(P_0\)。原单 \(B\) source 允许有附加零；它的导数列已经满射到完整 \(C\)，因此原完整 \(I_4\) 夹在同一个 \(C\) 的两侧而相等。结论不要求先准确重构整个特征零 \(B\) 或全部 \(M_g,\Gamma\)。

原 R825 给

$$
E=(y)_\infty=\mathcal D_{\rm cusp}+P_0+3D,\qquad \deg D=395,
$$

并在非 cusp 点以每层降一的原特征零导数公式计算 \(I_n\)。故 (835.3) 迫所有非 cusp 极点重数至多 4。非 \(P_0\) 的重数为 \(3d\)，在 \(P_0\) 为 \(1+3d\)；两种情形均给 \(d\le1\)。于是

$$
\boxed{D\text{ 是约化有效除子，}\quad K=1.}
\tag{835.4}
$$

未证明四阶是最小终止层，也未由此判定 \(P_0\) 是否属于 \(D\)。R825 的安全 395 层上界在这一个原对象上可由实际 \(K=1\) 取代。原逆递推现缩为

$$
I_D=\mathcal R\cap(I_1+r\mathcal R),\qquad r=y/\delta y.
\tag{835.5}
$$

(835.5) 的原完整坐标及其后 \(\eta\)/刚性化仍需实际完成；本结果不把理论接口写成这些输出已经得到。

## 4. 实际输出身份与小 IO

仓库仅保存本证明、脚本、参数和简明运行/SHA。完整节点、determinant/Bézout 系数和机器回执留在一日 artifact。

| 成员/对象 | bytes | SHA256 |
|---|---:|---|
| 最终原终止证书 | 4830 | 3221f24e080488f8832c32bf30d12323e7671202925ddce773c8ec07ef304c6c |
| core receipt | 508 | 16676243942f3b00d7673c4dbe12d577be8e86b0e5e9aff188ddd7ecb331821a |
| full manifest | 833371 | 2d77e2f090c6dd4ec2e6a4597667e0bf01003ee22694f11e78a1f797e3a217c7 |
| stage manifest | 214994 | e99a37cdaa1662f2f08c377e0f83d80e18ec068453468d0308456a397d1f58fe |
| \(a=0\) 完整 determinant | 8646 | 43b2935f834edee41c8bff17abd3e943679d636bd3855cdb9ac769ecfa2055bf |
| \(a=1\) 完整 determinant | 20005 | 4fdd896ad46b3a6832db112108976b56c1c2301b310991cf6998353eba279718 |
| 首个 Bézout 前缀 | 8592 | 7a35e43b2bd989441a17092f301f8c4ac184b924f91aca48b417fa828402ebb4 |
| gcd 1 的完整 Bézout 前缀 | 26305 | f8af3ab0b006af8c1fd48cf542f6fe0de01e28e25fbd8ed04cf54ebc6c24a2db |
| 新最小原 source carrier | 27499704 | eb908748fed6d68e49656f8df9f65212f849a2ffee672bf792eb63a2fd082962 |
| 原输入 carrier，字节不变 | 233593489 | 1e3fc4db60bb41a2daa592245257a1ab2e2522e3dccac4e3aaf5b9041926be44 |

新最小 carrier 名为 R827-determinantal-completed-source.tar.gz，保五层全部原 \(C\) 列/index 及必要原来源；旧 carrier 为 R827-retained-producer-inputs.tar.gz。full manifest 有 4901 项，ZIP 有 4903 成员；完整 verify 的 complete_stages 为 4892。读取既有输出的本地小 IO 只取 18 个小文件、1350917 B，逐 manifest SHA 绑定，没有下载 carriers、重算节点或执行数学。

artifact 为 14183161538，名 serre-global-R827-determinantal-Bezout-43767561191-1；277615420 B，平台 ZIP SHA256 为 7eaffd6a2be22aeaae2c1104c1c319baf6248efdd69c7f49c8ac6f956a2a9567，期限 2026-11-16 22:10:17 UTC。必要消费者须在到期前沿原字节继续保存。

冻结 core：4f2dc1192d2f95f902f03c2b9f0e875af7b3e04df58b8ae5bbe86072fb5b35b3；wrapper：7715eeb902a576a2290cf318219aaa62d93d79737a7f1e4afaeb12234d93f0e6。原 R827 证明 SHA 为 17e9c828e01e652b1a73281bf2249ae2b39133faae3cf22384a5fd6d6a3d4a71；determinantal 证明 SHA 为 7e07f78eace749b130f0d1b7920f6c6a03c7f54a15b4e940749a69c060d89fbf。

## 5. 后继与边界

原同核 Hermite 续算 run 43764014099 已在数学上被此成功证书替代。取消 API 返回 HTTP 403 Resource not accessible by personal access token，故不登记“已经取消”；它自行结束后不再续接。已成 source 从这里的新 carrier 接续。

下一项是原 \(D\) 的准确 RR/理想表示、原 \(\eta\) 与高度所需输入。R787/R824 的真实准确关系、R815 的特征零算子工程仍各按原断点继续。主目标仍为 OPEN，固定 p41 的这条约化性结论不替代全部 p 的高度或同一 primitive/Legendre 标签非零。
