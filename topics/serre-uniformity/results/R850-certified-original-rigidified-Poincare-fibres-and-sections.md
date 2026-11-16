# R850：原五组刚性化 Poincaré 纤维、完整截面及帧一阶项已构造

日期：2026-11-16。会话：serre-public-astra-20261115。

**状态：本项实际准确表达式完成。** 公开消费者已从原全局分式理想、真实点图和原 c0 首项，构造五组指定 Poincaré 非零纤维、主函数刚性化运输、完整 Picard 修正及基点归一截面的有限准确 DAG。共有 **330 个新表达式节点、11 项原非零依据、2 个完成数学阶段**，没有重新执行旧 Norm、点加法、CM 响应、Dixon 或全局线性解。

实际 [run 43796696213](https://github.com/Rogerhu12/math-research-public/actions/runs/43796696213)，compute job **133067102293**，源提交 **57b2899f61cb23b73bc7b8532f3ee2ae78d28206**。核心用时 **0.3978697619999707 秒**；run receipt 于 **2026-11-16T03:13:15.723953+00:00** 记录正常结束，退出码0、error=null、outer_timeout=false。工作流的数学步骤、输出核验和一日载体上传均真实成功。

## 1. 已完成的具体对象

固定[原 RF 证明](../notes/2026-11-16-original-c0-rigidified-Poincare-fibres-and-theta-section-DAG.md)和[执行契约](../notes/R850-original-rigidified-fibres-consumer-method.md)的所有规范。原
\(P_Y=[P_1-P_0]\in J_Y\)、\(\gamma=[c_1-c_0]\in J_X\) 与 \(\beta=q\gamma\in A\) 不混用。

| j | 原 \(p_j/q_j\) | \(\delta_j=p_j-q_j\) | 原 \(P_0\) 的 \(Z_j,Z_j^R\) 重数 |
|---:|---:|---:|---:|
| 1 | 165/67 | 98 | −686 |
| 2 | 93/67 | 26 | −182 |
| 3 | 100/67 | 33 | −231 |
| 4 | 168/67 | 101 | −707 |
| 5 | 371/134 | 237 | −1659 |

每一组输出包含：

- 原两图嵌入理想 \(I_{Z_j}=\mathcal O_Y(-Z_j)\) 与 \(I_{Z_j^R}\)，以及原 Picard 类的正确负号；原全局函数和理想节点保持来源引用。
- \(P_0\) 的帧 \(e_j=t^{-7\delta_j}\)、\(P_1\) 的帧1及真实纤维
  \(v_j=1(P_1)\otimes e_j(P_0)^{-1}\)；相同规范给 \(v_j^R\)。
- 原正乘主同构 \(I_{Z_j^R}=\mathcal R_j I_{Z_j}^{\otimes3}\)，其两端标量和刚性化运输
  \[
  v_j^R=\frac{\kappa_j}{\mathcal R_j(P_1)}\,v_j^{\otimes3}.
  \]
  这里是固定 Poincaré 第一槽、对第二槽取三次张量。
- 原六个完成 Norm \(M_h=s\,m_h\) 的实际有理坐标 \(m_h=M_h/s\)；完整原 \(K\) 式与等值有理式
  \[
  \nu_j=(3s)^{7\delta_j}\frac{M_f^{p_j}}{M_{g_j}^{q_j}}
       =3^{11\delta_j}\frac{m_f^{p_j}}{m_{g_j}^{q_j}}
  \]
  同时保留，不展开巨大整数幂。
- 原 Hom pullback theta 因子 \(S_j\)、实际 theta 帧值 \(u_j\)、真实 \(\mathbf Q\) 三次纤维和 canonical square
  \(z_j^{(3)}\in\mathcal P_{J_X}(\gamma,3\lambda_{S_j}\gamma)^\times\)。
- 完整 \(\operatorname{Corr}(S_j)\)，原 theta 二挠代表及其反向 Picard 因子一起运输；原基点归一截面
  \[
  \nu_j u_j^{\otimes3}\otimes v_j^R
   =\frac{\nu_j\kappa_j}{\mathcal R_j}\,
       u_j^{\otimes3}\otimes v_j^{\otimes3}.
  \]
- 与原 \(\mathscr N_h^{\,3q_j}\) 的唯一刚性化比较。原 \(C_h=c_{\rm clear}c_{\rm triv}\) 保持具名原常数，没有伪填其数值。

图中“乘 \(\nu_j\)”的标记只说明正向乘法，不断言 \(\nu_j\) 在某个实嵌入下为正。11项非零依据分别来自六个实际非零 Norm 及五个原 \(\mathcal R_j(P_1)\)；后者使用原 R843 非挠与 R844 Hom 值分离，未代入未被接受的短 CM 候选。

## 2. 两个帧的一阶项确实输出

令 \(d_j\) 为 [R848](R848-certified-original-c0-Hodge-jets-and-comparison-leading-coefficients.md) 表中已准确完成的单位首项系数。本次五组输出分别给

\[
-\frac{d_j}{2},
\qquad
-\frac{3d_j}{2},
\]

并以约分后的准确有理数保存。第一个属于原实下降理想帧，第二个属于较小理想的三次帧；五组均与原 \(p_j,q_j,\delta_j\) 和对应 C0 文件绑定。它们是**代数帧系数**，没有当作高度导数。

## 3. 三个真实直接来源和必要续传

| label | run / source commit | 实际选取原文件数 | 原数学内容 |
|---|---|---:|---|
| GLOBAL | 43790410670 / 391191590dcb8bcc6f8f2d777610726fa79dc2a3 | 12 | R849 的523节点全局函数、五极理想图及原必要载体 |
| C0 | 43790534424 / a576ab9d3b6d155027ec6f52cb689205ee5e9b98 | 19 | R848 六个 Norm、五个比较首项及来源元数据 |
| POINTS | 43789012126 / f699023d15daacb7d7e176f52da41899d69ae26c | 9 | R847 保留的原270件点/jet来源载体 |

三组共 **40 件**，选取来源集合指纹为
**25bd537ce0c9f573cff99eb731d948b55f268dcbdbf7d7748648ebf619973bc7**。

直接 POINTS 中再按原 receipt 解出并逐 SHA 核验270件；其中嵌套 POINTS 是 R844 的529节点原点图。原 Hom、CM、非挠、五方向和父子身份均保持；来源引用明确区分直接和嵌套标签。

GLOBAL 的 **395061658 B** 原载体保持完整原字节，其 SHA
**6a0a5d8cc918f1802662865dfaf254987f33086191ce01e9169ec789b5456703**
及2709件内层清单继续保留。本消费者不展开该大载体，不重新执行内层数学。C0旧大载体和 R847 的1413个有限精度阶段没有重复加入；它们的已完成准确结论作为原子来源消费。

新载体 **398650918 B**，保存全部40件必要直接输入及其中两份原载体。由此后继可继续使用原全局与点来源，不依赖这些上游 artifact 在到期后仍存在。

## 4. 实际输出与源码身份

| 项目 | bytes | SHA256 |
|---|---:|---|
| 新准确核心 | 28151 | ad8a8237092e907a44a4e4fc679ee40512afd980f801a6063b744a9fa3caa975 |
| 标准库包装器 | 40912 | ff318ca06e5bf2a385c866df2abb0ea102d6606eb2af2a818a0493f075b123cf |
| 最终证书 | 4420 | 11b3daca7c11ea37f41d6a56308664a14578719370b5fea22d6b3bbe43664676 |
| 330节点准确图 | 44145 | b3a8cd7fc0bf51506e8fcb45536d81ca861d9334268f6f44b229535c48824f68 |
| 来源审计 | 3175 | 1ed7a7408b40027bfaebb88f07840fb9138cbbd5635832408d3b8ceb5b5c30f2 |
| 两阶段 manifest | 1774 | aef09f7554e3848ff49d4556e00ffb5e456ddfed325df1e3be278912741e2186 |
| 全输出 manifest，12项 | 2159 | bcdfc8ce5c7d8f9e412651f7af51dfe93a4661613135f4810de3b7d9b06dd0e5 |
| 原输入 inventory | 9289 | 36a26242522d16832e202ccfcec2b73e6dbc30805c39b1e6c2d4ac53257c6ee1 |
| 新必要输入载体 | 398650918 | a4c38c0efd02433b501f62fc2e93b83dacd01299a8f8d5843cc0fadbfef92bc8 |

数学配置指纹
**8258917304ffb3fbe08cb674fb5115a626beb83ebe861d4afa709b90e1901d17**；
RF proof **e2b87b990914fe7b47bbbc10348a9f4512dd48da0e28dcddf1883ca42fa232f5**；
method **9fd821a471d90a43ba4c27d3a971b323747ea56b3f2da8f9869d6770b7154609**；
实际 request **bf0259b80da92d19499823555108a0873be72c220adcd6b06be156fb9ea07f30**。

入口：[请求](../notes/R850-original-rigidified-fibres-public-request.json)、
[核心](../scripts/R850_original_rigidified_fibres.py)、
[包装器](../scripts/R850_public_original_rigidified_fibres.py)。
工作流为 .github/workflows/serre-R850-original-rigidified-fibres.yml。

一日 artifact **14194427829**，名称
serre-global-R850-original-rigidified-fibres-43796696213-1；
ZIP **398744768 B**，实际平台 SHA256
**b466d4c1cb6e0b495e3ca1ba892406d9e51c771b75769505dfec2a8bd49a11c3**，
到期 **2026-11-17T03:13:19Z**。ZIP含12个输出、manifest和reference，共14个成员。

根会话以11次 HTTP Range 读取11个小输出及清单/引用，实际传输96291 B，逐件核对原 manifest/SHA，读回最终证书、两阶段、来源及五组帧系数。完整 ZIP SHA 来自真实 Actions/API；此小文件读取没有冒充本地已重哈希整份 ZIP或重新下载398MB载体。全部新数学只在公开 Actions，机器图、回执及载体不进入 Git或Release。

## 5. 下一输入已经具体，未解范围仍准确

准确图还给出原地方表达式

\[
\lambda_{v,h_j}
=\frac{\chi_v(\nu_j\kappa_j/\mathcal R_j(P_1))
       +\tfrac12\tau_{J,v}(z_j^{(3)})
       +3\tau_{Y,v}(v_j)}{3q_j},
\]

保持全部真实 \(\mathbf Q\) 纤维、原 splitting 和非p项。这个节点明确未求值。五组完整纤维及刚性化截面不再缺定义；指定 canonical Poincaré logarithms、实际高度数值、原高度非零、标准 Jacobian 坐标、A.1以及全p一致性仍未完成。后继直接消费本次准确图和必要载体，不再重跑旧来源或本次已成两阶段。

