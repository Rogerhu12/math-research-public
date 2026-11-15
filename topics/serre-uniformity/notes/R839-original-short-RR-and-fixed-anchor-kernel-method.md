# R839 执行契约：原齐次源到短 RR 商及固定锚核

日期：2026-11-15。数学依据为 R839 原证明、R838 的真实完整 $I_2$ 与 $P_0\notin D$、R837 的准确固定两锚。本文不预填新秩。所有新数学只在原公开仓库 Actions 运行。

## 1. 固定来源与实际新增运算

固定地方为原 R827 的 $\ell=1000000753$、原 branch0；$\zeta_3$ 的模像直接读原 place audit，不能另选另一分支。沿原 R805 的272维正规自由基，权为 $e=(0,1^{144},2^{127})$。

读取的五组原输入如下。

1. R827：原 place/unit audit；原 $B$ 乘法 index 的17个 row blocks；原第一导数 precision0010 的170个 coefficient row blocks；原第二导数 precision0012 的204个 blocks；已成的 `R827-prime-1000000753-S5-fixed-minor-inverse.json.gz`；必要原 metadata。前三层是原 normal $F$，不能用 $C^{-1}F$ 代替。旧 $B$、$\Gamma$、$M_g$、插值和导数不重算。
2. R838：实际成功 q2 证书及来源，明确 $J_2=I_2$、$\operatorname{mult}_{P_0}D=0$、$\deg E_2=415$。
3. R837：准确固定两锚及其成功1213子式、固定空间与原 metadata。锚的整数 $K$ 坐标、清分母尺度和原有序基全部保留。
4. R809：原1234个 S5 基行、原 basis index 与来源。所有69项/20坐标准确整数行只读；尺度仍为 $82^{10}$。
5. R786：原 power2 的418行与 power3 的690行、原 index/metadata。已有 $q_Y^0,\ldots,q_Y^{128}$，只读前69项；不重生任何旧 Fourier 系数。

wrapper 负责真实 run、manifest、byte/SHA、来源 carrier 与结束状态；core 按原 stage 的 complete/configuration 逐一核绑定，数学 stage 中仅保存真实源 spec。配置中的绝对目录不进入数学身份。

## 2. 统一权11的原子秩阶段

读取三个原矩阵多项式 $F_r(z)$，逐项核原权界
$$
\deg (F_r)_{bc}\le 5+e_c+2r-e_b.
$$
由系数移位拼出
$$
\Phi_{11}=\bigl[z^k(F_r)_{:c}\bigr]_{r,c,0\le k\le 6-e_c-2r}
\in\operatorname{Mat}_{2866\times2886}(\mathbf F_\ell).
$$
目标行依次为 $(b,j)$、$0\le j\le11-e_b$；源列为 $(r,c,k)$。这一步没有新的域运算推导或 Fourier 尾。

源列选择的 RREF 完成后立刻保存实际秩与原独立列 $J$。只有实际秩2451时才继续。随后对 $T=\Phi_{11}[:,J]$ 的转置 RREF 选出原行 $I$，计算原 $T[I,:]$ 的真实非零 determinant。转置 RREF 同时给
$$
\Pi_{11}(x)=x_R-T[R,:]T[I,:]^{-1}x_I.
$$
保完整415×2866模投影，准确乘回全部 $\Pi_{11}T=0$ 与 $\Pi_{11}[:,R]=I$。不求或保存2451阶特征零逆。特征零对象以原 source、$I,J$、原单位 solve 表达式定义，合法性由 R839 的准确包含及2451维上界保证。

若秩不足，保存真实结果并以未得充分证书结束；不能称原空间不存在或推翻 R838。不同更高统一权须由后继显式配置，不能本次冒称已经计算。

## 3. 原 T5 短商

原 $V_5$ basis 顺序为 $(b,j)$、$0\le j\le5-e_b$。通过 $\tau^6$ 与 $\sigma^6$ 的两个原嵌入，从 $\Pi_{11}$ 直接选列形成830×1234的 $K_5$。没有新乘法卷积。

其特征零秩由 R839 准确等于415。保存实际415阶非零子式、415个原独立行与对应商 $Q_5$。完整模乘回可证明所选行确为这次830行的整个行空间；特征零全行等价性仍由准确秩及原单位子式给出，不从模零猜测。

## 4. 同地方准确锚乘法与旧逆复用

R837 成功使用素数1000000009，故其已成模乘积不能冒充本次原地方1000000753。只读两锚的准确整数 $1,\zeta_3$ 坐标，用本次原 $\zeta_3$ 模像形成所需新前69项；所有原 $82^4$、$82^6$、$82^{10}$ 保留。

对每锚和每17个原 $V_3$ 基向量，计算原 $q_Y,\xi_{41}$ 双变量乘积。打包 stride79、截取69项，再完整模 $\Phi_{41}$ 约化。随后按原 $v=\xi_{41}^{-10}q_Y$ 相位改写并验证共轭对称，将40个坐标转换成20个原 $t=\xi+\xi^{-1}$ 坐标。

坐标转换只使用 R827 已成 S5 同素数 inverse。读取其原 row_indices 及 inverse，不重新求1234阶逆或旧 rank；对新产品用该逆解选行，然后在原全部1380坐标完整乘回。不能只验1234选行。新 target 与原 S5 行都含相同 $82^{10}$，不额外插入标量。

每个17列组原子保存新原产品、S5坐标、$Q_5$ 作用及全1380乘回旗标。完成组在续算时直接读取。锚不改，旧原 $V_3$ 顺序不改。

## 5. 原 D 的395阶短核

将两组 $Q_5M_u,Q_5M_v$ 拼成830×690矩阵。R839 给其准确特征零秩395、核维数295。实际 RREF 的源列与独立原行给真实非零395子式。

每个标准自由方向的准确基定义为原395阶单位选行 solve；原模基另存690×295，并完整乘回全部830行。只有395子式及所有来源接缝都成立，才设置
`exact_original_D_RR_space_as_unit_chart_expression_certified=true`。

这个输出是原 $H^0(3H-D)$ 的唯一准确特征零表达式及其实际模约化。它没有展开所有 $L$ 坐标，没有计算原 $\eta$ 或高度；后继如只接受展开坐标，应显式适配该 source DAG，不能改标签伪装。

## 6. 文件与断点

core 为 `scripts/R839_original_short_RR_spaces.py`；RESULT 为 `R839-original-short-RR-spaces-and-D-kernel`；FINAL 为 `p41-original-short-RR-and-D-kernel-certificate.json`。CLI：`--config --out --budget-minutes`。

数学 tag 固定 core/proof/method 哈希、五组原来源与逐文件 spec、原 prime/branch/尺度/矩阵顺序；目录、budget、实际 source-free 时间戳不入 tag。所有数学阶段为根目录 `R839-*.json.gz`，原子替换且 complete/configuration 一致。stage manifest 只列实际完成阶段，不包含自身；最终证书引用实际源和完成阶段。

预算停保已成秩、商、乘积组与核，不重算完成阶段。秩不足是一次诚实的充分检验未通过，final 的相关数学旗标保持 false。完整成功需 T11、T5 商、D 短核三项均成；`expanded_characteristic_zero_coordinates_computed` 和 `actual_eta_or_height_computed` 始终 false。

原始矩阵仅在一日活跃 artifact 内。Git 只保存脚本、参数、来源编号、哈希与证明，不保存可重算原始数据。
