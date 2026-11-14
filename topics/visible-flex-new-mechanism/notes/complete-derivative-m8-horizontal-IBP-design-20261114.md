# 完整 pure 导数成本的真实几何分部积分消费

日期：2026-11-14。R129、R130 的完整纸证已登记。本新消费源码已通过本地 py_compile 和六项人工小例检查；尚未运行研究消费。完整导数 pure 源已由 run 43652134080 成功发表，下文只绑定这一真实源。

脚本：[literature_derivative_m8_geometry_ibp.py](../scripts/literature_derivative_m8_geometry_ibp.py)。

## 1. 目标和原输入

本消费仅处理完整前一消费保存的两组原 packet：

$$
\widetilde L^{[2]}=L^{[2]}+\Delta L^{[2]},\qquad L^{[4]}.
$$

必须取得 literature_derivative_m8_tail_quotient.py 完整成功的主报告、public publication receipt 和 gzip 原证书。源脚本固定 SHA-256 为 5c7bb457eec0b68b31b2e7250cf89eb7901660ffac289ccf7854a8c47c198705。每个几何系数沿用三元记录 $(P,A,R)$，表示完整多项式、31 个已发原响应基列的系数、准确余项。

入口有八个显式 CLI 参数：

- --source-report；
- --source-report-sha256；
- --source-publication-receipt；
- --source-publication-sha256；
- --source-certificate；
- --source-certificate-sha256；
- --source-run；
- --source-commit。

全部入口必须来自真实已发表输出。本消费重新核对输入字节、原 gzip 字节、source_hashes、run、source commit、完整输出角色及 receipt 的 source_files/outputs。source main 如采用小摘要 fallback 仍可消费，但 completion 必须 complete 且完整证书存在。

本轮具体来源为 source commit `6e2f99ceda8f43e0cf5ade6ec3bbaebd1ea7f73b`，目录 `notes/actions-43652134080-1-derivative_m8_tail_quotient`：主报告 14890 bytes/SHA `20157415f95817dabfda88ca3b8914dfdbec058ae8c00d89a6c0a6ac8a9fe585`；receipt 33607 bytes/SHA `192a945b561d3a37ef1a454de91292df81de90bf60e4877565f6d0bd9362ffd9`；完整证书 gzip 1089774 bytes/SHA `68a764d03fc6f7d88a69dba624a92fa616d86b29b545777296aa7ad991b3c48d`。原文 9189672 bytes/SHA `ecdc5297777ab6ae30d9ff6ca35e1e9a21b633e0e60c91da42908d5e1c78a423`。

R116 的 31 个原响应多项式只作为原 packet 身份校验的基列读取。没有重新因式分解响应矩阵，也不重算其旧依赖，更不调用任何 profile 原式、m=8 代入或响应公式。

## 2. 完整十键的水平微分

坐标保持

$$
(h,k,\omega,u,w,a,b,\log h,j,\ell)
=(h,k,\omega,h_s,k_s,h_{ss},k_{ss},\log h,h_{sss},k_{sss}).
$$

对每一个完整 packet 作同样的有理线性操作。所有链式项为

$$
D_0=u\partial_h+w\partial_k+\frac{w}{2h}\partial_\omega,
$$

$$
D_s=D_0+a\partial_u+b\partial_w+j\partial_a+\ell\partial_b.
$$

对 $h^n(\log h)^m$ 同时保留 $n h^{n-1}(\log h)^m$ 和 $m h^{n-1}(\log h)^{m-1}$。没有把 $\omega$ 固定，也没有剪掉第三阶坐标。

## 3. R129 的两个准确消元

权二：从完整加速度线性项 $pa+qb$ 取 $P_1=pu+qw$，直接用完整多项式计算

$$
\widehat Q_2=L_2-D_sP_1.
$$

结果必须只含速度二次项。

权四：将每个 $B_hj+B_k\ell$ 移成 $P_{3,a}=B_ha+B_kb$，从完整原式减去 $D_sP_{3,a}$。这样自动保留新产生的加速度平方和系数链式导数。对剩余 $\bar C_ha+\bar C_kb$ 取

$$
P_{3,v}=\frac{u\bar C_h+w\bar C_k}{3},\qquad
\mathcal N_4=L_4-D_s(P_{3,a}+P_{3,v}).
$$

全部原式差必须准确为零，不只检查商余项。完整结果分为：

$$
\bar A_{hh}a^2+\bar A_{hk}ab+\bar A_{kk}b^2,
$$

$$
H(S;u,w)(ub-wa),\qquad \widehat Q_4(S;u,w).
$$

从 $b$ 的系数准确读取 $uH$，再同时核验 $a$ 的系数确为 $-wH$。因此两种可能的非对称项都在证书中，不会被三次势一起误删。所有状态微分产生的速度四次项同样保留。

## 4. 输出与边界范围

完整证书保存：

- 权一、权三的完整边界势及权三两部分；
- 完整 $\widehat Q_2,\mathcal N_4$ 和二者之和的全部 packet；
- 加速度二次部分、两种非对称项、完整 $H$ 和速度四次部分；
- 每部分的未分权、profile 分权、偶总次数响应商秩与全部原多项式关系；
- $L_j=D_sP_{j-1}+\mathcal N_j$ 对完整 $P,A,R$ 的零差检查。

紧凑 main 另加非阻断的 `normal_semantic_support`：分别对完整正规多项式、已知响应部分和完整商余项报告实际 min/max r、最大总次数、支撑数，以及所有 $r<25$ 项的几何系数数、单项系数数、原行列表和“是否全零”。R85/R88、R130 预测真实正规系数中低于 25 的尾幂应消失；本消费只观察真实结果，不按预测删项、不给它增加 failure gate，若不符仍保留完整 certificate。

首末常值 germs 给 $u=w=a=b=0$，所以这些明确的正导数权势分别在两端为零。无此条件就必须保留全部势端差。不会删除 R109 的权零端点势，也不删除固定连接基准。

若全部正规式商系数为零，可以结合 R124 和常值端口推出完整 pure 周期商为零。若不为零，输出仍只是准确的局部积分形式；本消费不宣布符号、实际可达维数、真实成本锥或 ruling。

## 5. 实际运行范围

建议 lane：derivative_m8_geometry_ibp。只需 scripts、完整导数消费的实际 notes 目录，以及 R116 的原响应 notes 目录；无需再读完整原 profile DAG、W-only 或 static 原数据。

建议公开命令：

~~~bash
python3 -m py_compile scripts/literature_derivative_m8_geometry_ibp.py
python3 scripts/literature_derivative_m8_geometry_ibp.py \
  --toy-only --out computations/run-derivative-m8-geometry-ibp/geometry-ibp-development.json
python3 scripts/literature_derivative_m8_geometry_ibp.py \
  --source-report notes/actions-43652134080-1-derivative_m8_tail_quotient/derivative-m8-tail.json \
  --source-report-sha256 20157415f95817dabfda88ca3b8914dfdbec058ae8c00d89a6c0a6ac8a9fe585 \
  --source-publication-receipt notes/actions-43652134080-1-derivative_m8_tail_quotient/receipt.json \
  --source-publication-sha256 192a945b561d3a37ef1a454de91292df81de90bf60e4877565f6d0bd9362ffd9 \
  --source-certificate notes/actions-43652134080-1-derivative_m8_tail_quotient/derivative-m8-tail-certificate.json.gz \
  --source-certificate-sha256 68a764d03fc6f7d88a69dba624a92fa616d86b29b545777296aa7ad991b3c48d \
  --source-run 43652134080 \
  --source-commit 6e2f99ceda8f43e0cf5ade6ec3bbaebd1ea7f73b \
  --max-seconds 240 --memory-mib 1024 --max-operations 3000000 \
  --out computations/run-derivative-m8-geometry-ibp/geometry-ibp.json
~~~

实际研究分支有公共 repo Actions 限制。完整证书上限沿用 raw 40 MB、gzip 4.5 MB，紧凑 main 95 KB，均由公开 Actions 终端 Git 保存。

## 6. 已执行的小人工开发检查

最终含非阻断语义摘要的版本，本地人工运行报告为 horizontal-IBP-artificial-development.json，5278 bytes，SHA-256 91b27c93e66c932cf754641c150c178c9f1c467c51364ab16dfc7cb05efa4ebc；0.004694312 秒，原六项全部通过，没有增加研究先验的通过门：

1. 人工 $\omega a$ 准确留下 $-uw/(2h)$；
2. 人工 $uj$ 准确留下 $-a^2$；
3. 人工 $uwa$ 准确留下 $(uwa-u^2b)/3$；
4. Laurent/log 的真实链式导数；
5. 完整三元 packet 的边界差恒等式；
6. 未读取研究输入，未评价实际 profile。

这些小例只检查新接口。没有用它们代替实际完整密度的结论，也没有运行尚未发表的新研究输入。
