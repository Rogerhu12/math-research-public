# 原完整二轮 210 列的逐来源生产接口

作者：Astra-ISP-789f / normal_annihilator，与 /root。AI-assisted GPT-6 Astra Pro。

## 1. 准确范围

原系数映射固定为 $(p,d)=(127,100)$。保持全部十二参数、十个模坐标及原十八生成元，不调用 Singular，不建立权九或权十稠密矩阵，也不重新消元。

输入的原首轮 106 列使用同一个已付字典：原 50 保留种子、全部 30 条 $N_iY_j$ 和完整权八选择的 26 条 $N_iC_\ell$。本入口新增恰 104 列：
$$N_pN_qY_j\quad(4\cdot6=24),\qquad N_pN_qC_\ell\quad(4\cdot20=80),$$
四条路径严格为 $(1,4),(2,3),(2,4),(3,4)$。参数权分别为九和十。

[二轮稳定闭包及完整 210 呈示](../results/R150-appendix-original-parameter-stable-closure-stops-at-two-and-complete210-presentation.md)已经用原二次、三次来源证明完整性。本入口另外支付 104 列的真实数组生产与逐原多项式乘回；二者不能混称同一次计算。

最终生产成功只给完整有限域模型，不证明 $e_0$ 在像内、不证明单位理想，也不把有限域 20/14 压缩提升到原 $E$。

## 2. 冻结文件

| 文件 | bytes | SHA-256 |
|---|---:|---|
| `2026-11-16-r150-original-two-round-complete210-sources127-789f.py` | 22547 | `9aeb996a38cd6eb3a76625697f043751a9ccf8fbf49aaf5259f9ddf9b71052dc` |
| `2026-11-16-r150-original-two-round-complete210-sources127-inputs-789f.json` | 5263 | `3f9f8e65b38463dfbf1bab7df3b2c582177dac19ffda009053e4be09e2088b4a` |

主源 blob：`9ab5efd0991b6d6285d9824667e31b7aec279b3d`。已实际 AST 解析通过，当前尚未因此声明数学运行完成。

运行时固定 Python 3.12.14、python-flint 0.9.0。原输入 gzip 的完整物理 SHA 不放宽；代码拒绝其它 Python 小版本。无需 native 编译器或 Singular。

## 3. 父范围与来源绑定

四个输入范围全部由已付小源和实际临时文件提供：

1. `original-ten-parameter-module127-v2`：完整原五个 $N_i,S_i$、十八生成元、全部原种子；完整 manifest 钉 `9120695a…`；
2. `original-parameter-seed-compression127`：全部 116 原种子的完整压缩表达数学负载钉 `a1d73ea1…`；
3. `original-mean-first-frontier127`：全部 30 条原第一均值像的描述符字典钉 `84602b54…`；
4. `original-complete-weight8-frontier127`：全部 100 条原第一交换子像描述符钉 `3f2c8d3b…`，完整关系和选择数学负载钉 `875b3bce…`。

所有完整 SHA、bytes 和 parent binding 在 inputs 中列明。代码同时核实际父回执的完成状态、来源 SHA、当前 manifest 与回执一致，以及所有所选 phase 的物理、解压逻辑和 binding 身份。

父 native elapsed 和 stdout 时间不当作数学身份；真实继续仍要求所用全部数学负载逐 SHA 一致。父输出可以从相同来源重新计算，但不能从别的 job 假定大型临时文件仍然存在。

## 4. 原十坐标与十八来源的逐列门

先完整核 50 条原边界恒等式
$$u_im-mN_i=AS_i,$$
九条字面一次/二次路径，以及全部原 106 列的 $mv=A\sigma(v)$。

对于一条新列，先取已经支付的完整第一像
$$v_1=N_qv,\qquad s_1=u_q\sigma(v)-S_qv.$$
程序从同一原种子重算并核其全部十个向量坐标、全部十八个来源坐标及原多项式乘回，不能只凭 phase 标签认作正确算子。然后计算
$$v_2=N_pv_1,\qquad s_2=u_ps_1-S_pv_1$$
并核
$$mv_2=As_2.$$

额外门为：十坐标全部只含十二参数；每个单项式的完整加权度恰九或十；全部新 104 条来源的 Bell 项系数严格为零。一次完整原乘回失败时不能保存为成功列。

新列按“均值家族、交换子家族；四路径次序；原 seed 次序”排序。固定原 20 个低交换子的 ID 与原 14 个高交换子的 ID 都与完整父数学字典核对，不新选主元或忽略标签。

## 5. CLI 与可分阶段预算

在同一工作目录使用以下共同参数：

~~~bash
python 2026-11-16-r150-original-two-round-complete210-sources127-789f.py \
  --model-source 2026-11-16-r150-original-ten-generator-parameter-module-field127-v2-789f.py \
  --model-out original-ten-parameter-module127-v2 \
  --compression-source 2026-11-16-r150-original-parameter-seed-compression127-789f.py \
  --compression-out original-parameter-seed-compression127 \
  --mean-frontier-source 2026-11-16-r150-original-mean-first-frontier127-789f.py \
  --mean-frontier-out original-mean-first-frontier127 \
  --weight8-source 2026-11-16-r150-original-complete-weight8-frontier127-789f.py \
  --weight8-out original-complete-weight8-frontier127 \
  --out original-two-round-complete210-sources127 \
  --through prepare --seconds 180 --memory-mib 768
~~~

之后只改变预算/阶段，保持来源、所有输入和同一输出目录：

| 阶段 | 建议数学预算 | 内存 MiB | 外层墙时 | 完成范围 |
|---|---:|---:|---:|---|
| `prepare` | 180 秒 | 768 | 240 秒 | 原 106 列、50 border、104 新字面标签完整核验 |
| `mean` | 120 秒 | 768 | 180 秒 | 全部 24 条新均值像 |
| `final` | 300 秒 | 1024 | 360 秒 | 全部 104 新来源及完整 210 列索引 |

预算取值是执行建议，不是实际用时预报。代码允许在同源同 binding 下续至 900 秒，前提是已有完整 phase。没有本入口的实际新列进展时，不宣称已经恢复了来源。

## 6. 完整事务、复用和错误范围

每一列先把全部十个向量和十八来源原乘回，随后保存完整 gzip，最后原子登记到 manifest。只有登记成功、物理/逻辑 SHA 全匹配并有同一来源和参数 binding 的 phase 可复用。

恢复时重新核所有实际父数学身份；已有成功新列的完整 payload、标签和验证状态逐一匹配。复用计数与本轮重新算术核验计数分别记录，不把复用称为重新计算。

若预算在一列中途到达，只有此前登记的完整列计入完成前缀；未登记的临时文件不会被认领为成功。没有大标准基进程或不透明候选可供猜测。

退出值：

- `0`：所请求阶段完成。`prepare/mean` 的状态是 `completed-prefix`；只有 `final` 的 104 列全部完成才是 `completed`；
- `75`：真实预算检查点，完整列数、phase descriptor 和错误类型在原回执中保留；
- `1`：内存或原核验错误，`parameters.error={type,message}` 明确保存。内存错误不冒充预算，不放宽任何数学门。

## 7. 项数上界与存储安排

当前没有新的实际项数。按原完整字典得到以下保守数学上界：

| 新列 | 向量最多项 | 原十八来源最多项 |
|---|---:|---:|
| 每个权九均值像 | 37874 | 16442 |
| 每个权十交换子像 | 77276 | 46304 |

来源项界使用十一条权四原梯度、六条权五原梯度和 Bell 系数严格为零。全 104 列向量项最多 7091056、来源项最多 4098928；这是全稠密字典上界，不是实际规模或运行测量。

程序最多保留六个第一像缓存，新列逐条封存后释放；不同时保留全部 104 个展开结果。旧 106 列只在最终索引中引用原父 phase，不复制到新大矩阵。每个 phase 记录实际向量项数、来源项数及来源 $u$ 次数；后续资源判断应使用这些实际记录。

## 8. 完整输出与理论边界

临时输出为：

- `complete210-sources-manifest.json`；
- `complete-original106-parent-validation.json.gz`；
- 24 个 `second-mean-*` 和 80 个 `second-commutator-*` 完整来源 phase；
- `complete-original210-source-model.json.gz`，内含全部 210 列的可复核引用；
- `complete210-sources-receipt.json` 及真实 stdout。

全部数学数组和 raw 留临时目录。仓库只存来源脚本、参数、证明与实际执行身份/SHA。

成功会得到两轮定理中完整有限域 $10\times210$ 模的实际来源数据。因为理论已另证第二轮稳定，不需要拿巨大权九/十消元作为完整性门。后续单位正证仍须给 $e_0$ 的真实原来源；特征零必须在原 $E$ 中另行准确核验，不能把本入口成功上提。

二轮论证的非 Bell 部分也可单独读取：原低交换子压缩、十四条换源及二次/三次降次均没有使用 Bell 列；因此原 26 条非 Bell 种子的二轮闭包由 200 列给出，呈示原十七梯度商。输出仍保存 210 列，只按原字典去掉十个字面 Bell 轴即可得到这 200 列，不冒称额外运行。全部新 104 列的 $s_{17}=0$ 是已冻结源码的硬门。它们的权为九、十，因而不改变原完整齐次权至多八的梯度像；这不排除 Bell 饱和后更高权的来源。
