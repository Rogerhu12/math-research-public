# R839 全局表达式第二次启动：原数域与初始 chart 的真实 schema

公开 run [43788533339](https://github.com/Rogerhu12/math-research-public/actions/runs/43788533339)，
job 133041569193，source `d39fa3789b95312b305c4676b312426519ae8c90`。
修复旧 R791 ZIP 后，八组 2709 个原输入已全部读取通过。
core `995a1298defa007a3f0447a91761a0fc1ad4bfe0ff6efc5a0ac99c76c77db59a`
在 0.627994246 秒、`Job.prepare` 的维数断言处退出，没有新数学阶段。

## 两处精准修正

原 R781 字段描述是完整
\(M^+=L(t_\xi)\)，不是只描述关系系数域 \(L\)：

- `dimension_over_Q=280`；
- 原基为 `B^i*s^j*t^r, j=0..1 outer, i=0..6, r=0..19 inner; B=lambda*b`；
- 原整 B 多项式有8项，实圆分多项式有21项；
- 原打包索引 `r+39*i+507*j` 保持原样。

因此只将描述器的误断言14改为280；关系未知数仍在14维
\(L=\mathbf Q(B,s)\) 中，每个原 Laurent 系数仍保20个实圆分坐标。
**没有改写原 field、换 twist 或删去任何坐标。**

相邻原 chart 的 `all_14_branches_already_verified` 实际为
`false`：它是最初持久化的 chart，早于后来全支证明。
该固定来源的断言改为原真实值，不把后来结论写回旧文件。
完整关系仍由后续绑定的 R840 原单位 chart 表达式提供：
同一原 field、同一 chart、完整129×20×14关系及“full kernel equals
selected kernel, dimension28”。原秩1186、自由列1186、其余自由列置零、
selection 各支互异及分母单位等条件未改变。

新 core 为48121B /
`544241acf5f3451df34c779d513ea6494616d4d4caa26cd2531749edc895aea7`；
wrapper `39bef61981f6c2193e64cd1797331a0ce9340ed468fc93dc785d8994c8d2a541`
不变。相对实际旧核仅上述两处来源断言和说明变动。
原全局数学 DAG、八个单位解、F/W/C/S5、GP 三子式/重数/负理想类号、
三同源正乘及真七 σ Norm 全部不变。仍无全局最终输出、规范理想格、
Poincaré 刚性化或高度结论。

## 原来源与实际失败 pins

| 来源 | 字节 | SHA-256 |
|---|---:|---|
| R781-original-real-field-input.json.gz | 833786 | 528720fe45edf23c1d065c034bd4d8be3c2e2905e45079d9e4a5c71015f7b5b1 |
| R787-prime-1000000753-chart.json.gz | 5829 | 47ac1ce2a95781417a4e3b51f2128d2dd4836e5d1793cf2a50793911dcedce96 |
| R840 原 implicit-expression | 72708 | 21cc66ed9a40a856edea495080ef2e375aefea6c6f17d6c26741b85e2f174342 |
| 失败 run manifest | 1425 | 1a81c7689f1345d7e7226eedbb90aa6eb4ea0608924e7d4bc05efb61a8e9d78e |
| 原输入 inventory | 449832 | e9a986c45970f2d16ac2ee054e22ab4ce01de7b19f5d8eb224018d66d686a9d0 |

一日 artifact `14191591612`，395994345B /
`687028dfb55b2b6f8c4eafc68e523249de972ca23d4f859dfad26d500f9b4948`。
本地只通过11次 Range读取7件小文件（934386B）和既有原来源字段，
没有下载该大载体、导入数学核心或运行新数学。
