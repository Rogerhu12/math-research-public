# 请求102首读回超限与v2显式摘要

**类别：读取工程事实；不是第98轮科学失败。**

首读回 [run43680444618](https://github.com/Rogerhu12/math-research-public/actions/runs/43680444618)，source854add3304e88b9d9262a15d9df72de8cd849b9b、job132709690650。原809042943B ZIP的size/SHA通过，五主要文件全部完整读取并按各成员CRC/原SHA记录。随后摘要474627B超90000B限制，SHA4a8049875734771ada1771ac0ca349cd62b7df03edbab8ad311883406d0d2a9c；未输出这份大摘要，未截去trial，未重算科学。

| 原文件 | 原字节数 | SHA256 |
|---|---:|---|
| model-000.json | 736781 | e2957f2d413653ea08c7f893f7cc3584c05450ff2ccb8c761d8109cfef1dfa6a |
| driver-status.json | 3379453 | b7ad389fad867fecf85edc4313145980d6e8686f207acf781ff6a050e7eae6ff |
| condensed-QP-summary.json | 121691 | a898e81af8f915b55c2db1607a775c28a89eaae1e782735fb133183c8963ec07 |
| response-check.json | 2648609 | b41e3f6d66f7d7a5bb0b4e6a6e0de56a1fc07c7c648044a86e5d012ea8b99385 |
| warm-001.json.gz | 4927052 | b59f40c003bf924f3f3c10aa6783425a606b3e395fd86311cbba159b835feb67 |

warm解码后14864483B，SHAa09ebdf16eae595e16694fe2b3443d0364f5319bb3a5e1a711ed123ace0bff30。上述是reader实际原日志，不冒其他ZIP数组载荷已审。完整原科学身份/参数与第一次读取接口见[102原接口](2026-11-15-request102-existing98-scalar-readback.md)。

通用深递归摘要把observer的source_entry历史producer反复展开，导致重复。v2仅改摘要选择：显式复制原domain/RMS失败点、完整trial顺序、31query定义、最终scalar/flags、QP选择和FD主要误差；历史producer树与source-map改成明确标注的canonical decoded-subtree hash，该hash不冒原文件hash。大数组、各FD level历史不复制；所有原文件身份仍保留。90KB限制和全部科学接受条件不变。

当前reader26301B，SHA256 `68f7c017dea3645b8a7ac3a9030fa5b7c68e4c300025c1245030bf62f342d61d`，schema后缀v2；transport/ZIP/五件读取/main正文与v1逐字相同。workflow SHA256 `72fd003d9e6b2a274aedf45b65628dd7bce92196ead538b79191d6c1f34dfb49`，request SHA256 `62b06d000dd267fea2f83f99e0a7f1b9f96a196a781d302a316f7150a36d0dcd`。继续在Actions只读原98，成功后保存真正科学结论；无新artifact/Release/Git原数据保留。未声称本地AST或新科学执行。
