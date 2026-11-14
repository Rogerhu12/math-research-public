# 冻结批次03：M12、有限深度与真实多模cut路径

会话 Astra-visible-flex-950f9f73 / nonlinear_tail，2026-11-09。
所有文件仍是有限频率/有限深度诊断；没有完整闭曲面完成声明。

## 已完成结果

- 同一物理metric、纯a=.0003、parts2×32步/profile：M12 fullD1.68347204e-9，
  actualMetric5.67546010e-13。与此前M4/M8形成角向加密序列。
- M12 depth10→12：cut slope最大差1.73472348e-18、mean correction不变。
  有限深度稳定不等于无限非线性尾证明。
- 冻结宏观prefix的8个cut Fourier系数，真正非线性tail DN延拓lambda
  .236135294→.67；lambda=.67的H1=-.000851206965，shoot2.01296e-10、
  fullD9.27755e-4、metric4.66942e-7、minA=.14844。
  下一步lambda=.70在初始root失败，保存了完整失败响应。没有不存在性结论。
- 全部高幅多模结果均未与其原来的linear-DN prefix导数匹配。实际coupling由
  macro_prefix的独立分支进行，不能将两类结果混用。

## 代码变化范围

`950f-tail-stage-port-v2.mjs` 仅向warm初值加上新的完整Dirichlet差的
线性响应，不修改full momentum root、PDE、mean/holonomy或验收。
v3新增`950f-tail-warm-remesh.mjs`，支持细化stage或增加有限depth，
所有新增节点都是初值，仍须随后通过真实非线性求解。

`950f-tail-boundary-path-v2.py` 对M8宏观cut向量逐lambda请求真实DN；
`950f-tail-stage-run-v3.py` 完成了M12 depth12重跑。
`950f-tail-boundary-path-v3.py` 已写好，但本批次不含其正在运行的
M12大振幅输出，后续另冻结。

旧慢边值初值路线已中断，保留stopped metadata与trace；它不构成失败的
几何证据。当前v2路线已解同一初始请求。

## 最小重跑

在topic目录运行：

```bash
python scripts/950f-tail-stage-run-v3.py --config notes/2026-11-09-950f-tail-k6-m12-depth12-config.json --source-root /workspace/scratch/1dce210849f9/math-research --out notes/replay-depth12.json --amplitudes .0003 --node-heap 1024
python scripts/950f-tail-boundary-path-v2.py --config notes/2026-11-09-950f-tail-k6-m8-prefix-fine-config.json --source-root /workspace/scratch/1dce210849f9/math-research --height-file notes/2026-11-09-950f-prefix-macro-m8-geometry.json --out notes/replay-prefix-fine.json --scales .55 .58 .61 .64 .67 .70 --node-heap 1024
```

重跑须使用新out与新trace路径；搬移工作区只修改I/O路径，不改物理参数。
所有真实依赖由各response源哈希和本批次manifest标识。
进度快照是`2026-11-09-950f-tail-checkpoint-03-progress.md`；活动progress仍会更新。

## 无限尾接口

`2026-11-09-950f-tail-effective-tail-interface.md`列出从actual raw7/8小量
到真正无限续接所需的连续解析小球、Green界、余项界、远端缺陷修正与全cell
Cartesian C2界；目前没有全部完成。三重旋转对称的平移period引理已单独写出，
不把它误作完整R46常数迁移。
