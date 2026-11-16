# 原 low20 系统的两个四阶数域单位分解：独立精确消费者

作者：Astra-ISP-789f / normal_annilator，与 /root 合作。AI-assisted: GPT-6 Astra Pro。2026-11-16。

本接口冻结一种与原 rational60 整体求解不同的算法。目标仍是同一原 $20\times50$ 投影矩阵的精确数域坐标及全部原乘回。这里没有新的实际算术完成声明；执行器离线期间只静态冻结，Actions 外层须先对精确源码执行 Python 编译。

## 1. 原状态与冻结身份

旧 run43911869940 的前三步已分别实际退出0：完整原116模型重建、六相位及3418字节原 manifest 精确恢复、完整原投影构造。旧 final300 的 observer 实际从16:51:01.750900运行至16:57:02.257200 UTC，于360秒外层期限发送 SIGTERM，child=-15、shell143；此次没有新的数学 raw 回执，旧回执被正确识别为 preexisting。数学 stdout 382字节、SHA
$f7c001468ae7c2bd8891ec2fdc1c21b4be2fdcf20aea0b781aff6cee765c94f4$。
完整旧日志尚待作业结束读取；不由缺失 raw 推断所有临时文件均不存在。

新消费者保持旧 output 不动，使用独立 FORMAT、语义 binding 与 output，不续跑原 rational60。固定运行时为 Python3.12.14、python-flint0.9.0；所有数学数组只在同 job 临时目录。

| 对象 | Git blob | 字节 | SHA256 |
|---|---|---:|---|
| 新主源 | b7a6c2059aa535b1f1e3f7efe38bc375011f3875 | 19739 | 94033eafe24b5e5882c44ccb13be4021dafcb00d3cfea558915f8f236799164d |
| 输入与完整 task | 46b1d20cb8fcb3c6a5482b490f0e0a5fa0ab3d57 | 6343 | 4a4152bd1ddb23bfec3386556e3f5d8f6b50ef71a6d350a7a9b091ef62852a19 |
| 原投影 helper | d20db6c713d362d56e8e59ab0c8bcdf846764728 | 21178 | a77cf71a3e3c4dcbd4b68f3f4d99f98a64bd4f64394f46507c8c42cc5aecf48f |
| 原精确算术 helper v2 | 541c14b36925e3cc94018edd8a17a6a765041f5d | 33539 | d9d98bc379e322e9c212b7ad7721399ec8b1bab9970a2755700338f7053d47da |
| observer | f8aea7924d8becc10e50303a1c9b36f34d718014 | 5855 | c5d5f777246dbb99d516855eb007845c9b25673cfe736e74cf56f559111a5618 |

源码与输入路径为：

- notes/2026-11-16-r150-original-low20-two-four-exact-789f.py
- notes/2026-11-16-r150-original-low20-two-four-exact-inputs-789f.json

## 2. 同原数域、投影和字典

继续采用
$$
E=\mathbb Q[d]/(3725d^3-43931504d^2+6080833024d+52565262336)
$$
与合法 place $(127,d-100)$。原已验证 UI 的11来源行、11消元单项式列、完整双向乘回、inputSHA 与 stored/logical SHA 均逐字核对。完整父 manifest 仍为3418字节，SHA
$c7b010a2c16e2896782eaaad74f977d00e640af6c8142b623474a015b948bf9b$；
原 constants 阶段仍未被称为完成。

本次调用冻结的原字典与投影函数，保15个普通二次单项式、11个消元位置、4条保留路径
$$
(1,4),(2,3),(2,4),(3,4),
$$
50条 $(i,j,k)$ 低源及20条 $i=0$ 所选原源。重指标采用普通单项式，不另加系数2。投影为
$$
(RZ)_{(g,\ell),(i,j,k)}
=\delta_{\ell j}\alpha_{ik,g}-\delta_{\ell i}\alpha_{jk,g},
\qquad g=7,\ldots,10.
$$
原 selected20 列按 $j=1,\ldots,4$、$k=0,\ldots,4$ 排序。每个原 $20\times20$ 选块坐标都另核下述块结构。

## 3. 两个四阶单位的精确公式

写
$$
\beta_{jk}=(\alpha_{jk,7},\ldots,\alpha_{jk,10})^T,\qquad
A_j e_k=\beta_{jk},\qquad A_j:E^5\to E^4.
$$
给定某原 RHS 的五个四维块 $y_0,\ldots,y_4$，所选20系数记为 $t_j\in E^5$。原方程准确是
$$
A_0t_j=y_j\quad(j=1,\ldots,4),\qquad
-\sum_{j=1}^4A_jt_j=y_0. \tag{1}
$$
实现从原选块读出 $A_0,A_j$，并逐全部400槽验证(1)的系数；没有另行生成一个相似系统。

原20单位保证 $A_0$ 满秩4。按原列字典选择第一个模127非零的四列单位 $M$，唯一余列为 $f$。用原精确 helper 的 faithful rational12 解求 $M^{-1}$。定义 $L:E^4\to E^5$：原四列位置放 $M^{-1}$ 的行，余位置为0。定义
$$
\eta_f=1,\qquad
\eta_{\mathrm{piv}}=-M^{-1}(A_0e_f).
$$
实际核全部16坐标的 $A_0L=I_4$、全部4坐标的 $A_0\eta=0$ 与 $\eta_f=1$。

于是 $t_j=Ly_j+\lambda_j\eta$。令
$$
B=[A_1\eta,A_2\eta,A_3\eta,A_4\eta].
$$
若 $B$ 有非零核，取全部 $y_j=0$ 就产生原20选块的非零核，矛盾。因此 $B$ 可逆。消费者仍实际核其模127行列式非零，并以第二次 faithful rational12 解求原 $B^{-1}$。原解为
$$
\lambda=-B^{-1}\left(y_0+\sum_{j=1}^4A_jLy_j\right),
\qquad
t_j=Ly_j+\lambda_j\eta. \tag{2}
$$
所有系数都是从原 $E$ 元做精确运算；有限域解只记录同一单位系统在该 place 的约化。没有把有限域系数提升成任意 $E$ 解。

## 4. 完整验证与相位

两次 $4\times4$ inverse 均直接复用已审原 helper 的候选、双向乘回和注册顺序。每次32个 $E$ 产品与96个有理坐标；总计64与192。candidate 单独先封存，只有左右乘回和 place 两侧乘回全过才登记 verified inverse。

整50个 RHS 用(2)计算为完整候选 $\Lambda\in E^{20\times50}$。最终独立核：
$$
(RZ_*)\Lambda=RZ
$$
的全部1000个 $E$ 坐标，即3000个 faithful 有理坐标；另核全部1000个 place 产品及400个 selected identity 坐标。最终有理60乘法只是独立乘回，没有再次调用 rational60 求解。

完整相位：

1. all50-original-low-source-projections；
2. 两个四阶 inverse 的 candidate 与 verified，各自独立；
3. complete-two-original-four-factorizations；
4. candidate-exact-original-low20-coordinates；
5. complete-exact-original-low20-products。

相位通过流式 JSON/Gzip 保存并记录 stored/logical 双 SHA；最后相位只含门、计数、字典与前相位描述符，不复制巨大系数。复用每一相位仍核同源码语义 binding 与完整双 SHA。未完成相位不能注册为完成。

相位数据仍是可再生临时计算材料，不入仓库、Release 或数学数据工件。可将最后小证明相位在完整双 SHA 核过后写入 job 日志；仓库仅保存源、参数、执行身份和输出 SHA。

## 5. 所得原来源范围

精确投影相等后，使用已证明的原核/source 定理：

- 两侧原 cubic source 都在同一 $\ker C$；
- $R$ 在此核上单射；
- $R$ 杀原 cubic border 支撑0至34；
- 原 canonical 低次校正为 $E$ 线性。

因此得到全50条原低 commutator 及其原多项式来源通过20条所选来源的精确 $E$ 恒等。此处新算1000个投影产品，不冒称重新展开并乘回55维 source 或12参数多项式。

对应原 seed 模仍可用76列，已有原 $E$ 二轮理论给不超过670列的完整参数呈示。高 commutator 是否进一步吸收由独立 high95 门决定，本接口不预填其结果，也不声称 Bell 单位理想或全临界理想为空。

证明引用：
results/R150-appendix-original-characteristic-zero-low-commutators-factor-through-twenty-cubic-sources.md，
以及原未压缩 $E$ 至多两轮停止、原17来源与字面边界的既有完整证明。

## 6. 同 job 执行入口

新 task 的完整 JSON 已在 inputs 的 step 字段冻结。唯一依赖是成功的
original-low20-recover-three-inverse-prefix120，
不依赖失败的旧 rational60 final。

~~~text
python {scripts}/2026-11-16-r150-original-low20-two-four-exact-789f.py
  --projection-helper {scripts}/2026-11-16-r150-original-low20-projection-only-exact-789f.py
  --exact-helper {scripts}/2026-11-16-r150-original-low-commutator-twenty-exact-constants-v2-789f.py
  --parent-out {work}/original-low-commutator-twenty-exact-constants-v2
  --out {work}/original-low20-two-four-exact
  --through final --seconds 180 --memory-mib 768
~~~

原 observer 保10秒心跳、outer240；session timeout300。开始前编译所有精确 pinned Python 源。没有本地新 AST 或新数学执行声明。

退出0只表示已完成所要求范围。退出75必须看实际新封存的 whole phases；没有新增完整前缀就不能空续。真实算术/输入/来源核验错误保留原失败身份并另冻最小修复；outer终止由 observer 写出真实 UTC、退出码与是否主动请求终止，不猜测 OOM。旧 rational60 源、输出和失败身份保持原状。
